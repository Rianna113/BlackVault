import asyncio
from core.session_manager.session_manager import SessionManager
from core.encryption.encryptor import Encryptor
from utils.logger import Logger

class TransportLayer:
    def __init__(self):
        self.session_manager = SessionManager()
        self.logger = Logger('INFO')
        self.connections = {}

    async def connect(self, peer_id, address):
        reader, writer = await asyncio.open_connection(address[0], address[1])
        self.connections[peer_id] = (reader, writer)
        self.logger.info(f"Connected to {peer_id} at {address}")

    async def send_encrypted(self, peer_id, plaintext):
        session_key = self.session_manager.get_session_key(peer_id)
        if not session_key:
            self.logger.error(f"No session key for {peer_id}, cannot send message")
            return
        encryptor = Encryptor(session_key)
        ciphertext, tag, nonce = encryptor.encrypt(plaintext)
        message = nonce + tag + ciphertext
        _, writer = self.connections.get(peer_id, (None, None))
        if writer is None:
            self.logger.error(f"No connection for {peer_id}, cannot send message")
            return
        writer.write(len(message).to_bytes(4, 'big') + message)
        await writer.drain()
        self.logger.info(f"Sent encrypted message to {peer_id}")

    async def receive(self, peer_id):
        reader, _ = self.connections.get(peer_id, (None, None))
        if reader is None:
            self.logger.error(f"No connection for {peer_id}, cannot receive message")
            return None
        length_bytes = await reader.readexactly(4)
        length = int.from_bytes(length_bytes, 'big')
        message = await reader.readexactly(length)
        nonce = message[:12]
        tag = message[12:28]
        ciphertext = message[28:]
        session_key = self.session_manager.get_session_key(peer_id)
        if not session_key:
            self.logger.error(f"No session key for {peer_id}, cannot decrypt message")
            return None
        encryptor = Encryptor(session_key)
        try:
            plaintext = encryptor.decrypt(ciphertext, tag, nonce)
            self.logger.info(f"Received and decrypted message from {peer_id}")
            return plaintext
        except Exception as e:
            self.logger.error(f"Decryption failed: {e}")
            return None
