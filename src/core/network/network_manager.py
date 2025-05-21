import socket
import threading
import struct
from core.session_manager.session_manager import SessionManager
from core.encryption.encryptor import Encryptor

class NetworkManager:
    def __init__(self, host='0.0.0.0', port=9000):
        self.host = host
        self.port = port
        self.session_manager = SessionManager()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((self.host, self.port))
        self._recv_thread = threading.Thread(target=self._recv_loop, daemon=True)
        self._recv_thread.start()
        self._listeners = []
        self._running = True

    def _recv_loop(self):
        while self._running:
            try:
                data, addr = self._socket.recvfrom(4096)
                peer_id = addr[0] + ':' + str(addr[1])
                self._handle_message(peer_id, data)
            except Exception:
                continue

    def _handle_message(self, peer_id, data):
        # Assuming first 4 bytes: message length, next N bytes: nonce, tag, ciphertext
        try:
            length = struct.unpack('!I', data[:4])[0]
            payload = data[4:]
            nonce_len = 12
            tag_len = 16
            nonce = payload[:nonce_len]
            tag = payload[nonce_len:nonce_len + tag_len]
            ciphertext = payload[nonce_len + tag_len:]
            session_key = self.session_manager.get_session_key(peer_id)
            if session_key is None:
                # Could trigger handshake here
                return
            encryptor = Encryptor(session_key)
            plaintext = encryptor.decrypt(ciphertext, tag, nonce)
            self._notify_listeners(peer_id, plaintext)
        except Exception:
            # Log or ignore
            pass

    def _notify_listeners(self, peer_id, message):
        for callback in self._listeners:
            callback(peer_id, message)

    def register_listener(self, callback):
        self._listeners.append(callback)

    def send_message(self, peer_id, message: bytes):
        session_key = self.session_manager.get_session_key(peer_id)
        if session_key is None:
            raise Exception("No active session with peer")
        encryptor = Encryptor(session_key)
        ciphertext, tag, nonce = encryptor.encrypt(message)
        payload = nonce + tag + ciphertext
        length = struct.pack('!I', len(payload))
        packet = length + payload
        ip, port = peer_id.split(':')
        self._socket.sendto(packet, (ip, int(port)))

    def stop(self):
        self._running = False
        self._socket.close()
