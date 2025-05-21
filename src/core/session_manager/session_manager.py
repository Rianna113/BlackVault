import threading
import time
import os
import hashlib
from crypto import DiffieHellman  # Assuming you have a crypto module

class SessionManager:
    def __init__(self):
        self.sessions = {}
        self._lock = threading.Lock()

    def start_handshake(self, peer_id):
        with self._lock:
            if peer_id in self.sessions:
                raise Exception("Session already exists")
            dh = DiffieHellman()
            public_key = dh.get_public_key()
            self.sessions[peer_id] = {
                'dh': dh,
                'state': 'handshake_started',
                'session_key': None,
                'last_active': time.time()
            }
            return public_key

    def complete_handshake(self, peer_id, peer_public_key):
        with self._lock:
            if peer_id not in self.sessions:
                raise Exception("No handshake started")
            dh = self.sessions[peer_id]['dh']
            shared_secret = dh.compute_shared_secret(peer_public_key)
            session_key = self._derive_session_key(shared_secret)
            self.sessions[peer_id]['session_key'] = session_key
            self.sessions[peer_id]['state'] = 'active'
            self.sessions[peer_id]['last_active'] = time.time()
            return session_key

    def _derive_session_key(self, shared_secret):
        # Simple key derivation using SHA-256
        return hashlib.sha256(shared_secret).digest()

    def get_session_key(self, peer_id):
        with self._lock:
            session = self.sessions.get(peer_id)
            if session and session['state'] == 'active':
                session['last_active'] = time.time()
                return session['session_key']
            return None

    def end_session(self, peer_id):
        with self._lock:
            if peer_id in self.sessions:
                del self.sessions[peer_id]

    def cleanup_expired_sessions(self, timeout_seconds=3600):
        with self._lock:
            now = time.time()
            expired = [pid for pid, sess in self.sessions.items()
                       if now - sess['last_active'] > timeout_seconds]
            for pid in expired:
                del self.sessions[pid]
