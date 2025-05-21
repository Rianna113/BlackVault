import threading
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from core.crypto.diffie_hellman import DiffieHellman
from utils.logger import Logger
import time

class Session:
    def __init__(self, peer_id):
        self.peer_id = peer_id
        self.session_key = None
        self.last_active = time.time()

class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.lock = threading.Lock()
        self.logger = Logger('INFO')

    def initiate_session(self, peer_id):
        self.logger.info(f"Initiating session with {peer_id}")
        dh = DiffieHellman()
        public_key = dh.get_public_key()
        # Normally, send public_key to peer and receive peer's public key...
        # For demo, simulate handshake immediately:
        peer_public_key = dh.get_public_key()  # In reality, get from peer
        shared_secret = dh.compute_shared_secret(peer_public_key)
        session_key = HKDF(shared_secret, 32, b'BlackVault Session', SHA256)
        with self.lock:
            session = Session(peer_id)
            session.session_key = session_key
            self.sessions[peer_id] = session
        self.logger.info(f"Session established with {peer_id}")

    def get_session_key(self, peer_id):
        with self.lock:
            session = self.sessions.get(peer_id)
            if session:
                session.last_active = time.time()
                return session.session_key
            return None

    def expire_sessions(self, timeout_seconds=3600):
        now = time.time()
        with self.lock:
            expired = [pid for pid, s in self.sessions.items() if now - s.last_active > timeout_seconds]
            for pid in expired:
                self.logger.info(f"Expiring session {pid}")
                del self.sessions[pid]
