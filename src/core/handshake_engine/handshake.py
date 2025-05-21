import os
import time
import threading
from cryptography.hazmat.primitives.asymmetric import x25519, ed25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

class HandshakeTimeout(Exception):
    pass

class HandshakeEngine:
    HANDSHAKE_TIMEOUT = 3  # seconds

    def __init__(self, role: str):
        if role not in ('client', 'server'):
            raise ValueError("Role must be 'client' or 'server'")
        self.role = role
        self.ephemeral_private_key = x25519.X25519PrivateKey.generate()
        self.ephemeral_public_key = self.ephemeral_private_key.public_key()
        self.peer_public_key = None
        self.shared_secret = None
        self.session_keys = None
        self.handshake_complete = False
        self._timeout_timer = None
        self._lock = threading.Lock()
        self._start_time = None
        self._ed25519_signing_key = ed25519.Ed25519PrivateKey.generate()
        self._ed25519_verifying_key = None

    def start_handshake(self, peer_public_bytes: bytes):
        with self._lock:
            self._start_time = time.time()
            try:
                self.peer_public_key = x25519.X25519PublicKey.from_public_bytes(peer_public_bytes)
            except Exception as e:
                raise ValueError(f"Invalid peer public key bytes: {e}")

            # Compute shared secret
            self.shared_secret = self.ephemeral_private_key.exchange(self.peer_public_key)

            # Derive session keys using HKDF-SHA256
            self.session_keys = self._derive_session_keys(self.shared_secret)

            # Start timeout timer
            self._timeout_timer = threading.Timer(self.HANDSHAKE_TIMEOUT, self._on_timeout)
            self._timeout_timer.start()

            # Simulate handshake completion for demonstration purposes
            # In real implementation, you'd perform signature exchange and verification
            self.handshake_complete = True
            self._timeout_timer.cancel()

    def _derive_session_keys(self, shared_secret: bytes) -> dict:
        # Derive two keys: encryption_key and mac_key
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=64,
            salt=None,
            info=b'BlackVault Session Keys',
        )
        key_material = hkdf.derive(shared_secret)
        return {
            'encryption_key': key_material[:32],
            'mac_key': key_material[32:]
        }

    def is_handshake_complete(self) -> bool:
        with self._lock:
            return self.handshake_complete

    def get_session_keys(self) -> dict:
        if not self.handshake_complete:
            raise RuntimeError("Handshake not complete")
        return self.session_keys

    def _on_timeout(self):
        with self._lock:
            if not self.handshake_complete:
                self.handshake_complete = False
                # Trigger kill switch or shutdown logic here if needed
                raise HandshakeTimeout("Handshake timed out")

    def get_ephemeral_public_bytes(self) -> bytes:
        return self.ephemeral_public_key.public_bytes()

    def get_ed25519_public_bytes(self) -> bytes:
        return self._ed25519_signing_key.public_key().public_bytes()

    def zeroize(self):
        # Overwrite sensitive data
        self.ephemeral_private_key = None
        self.shared_secret = None
        self.session_keys = None
        self._ed25519_signing_key = None
        self._ed25519_verifying_key = None
