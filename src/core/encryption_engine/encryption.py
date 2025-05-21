import os
import threading
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives import constant_time

class EncryptionEngine:
    def __init__(self, session_keys: dict):
        self._lock = threading.Lock()
        self.encryption_key = session_keys['encryption_key']
        self.mac_key = session_keys['mac_key']
        self.cipher = ChaCha20Poly1305(self.encryption_key)
        self.nonce_counter = 0
        self.KEY_ROTATION_THRESHOLD = 10000  # packets
        self.packet_count = 0

    def encrypt(self, plaintext: bytes, associated_data: bytes = b'') -> bytes:
        with self._lock:
            nonce = self._generate_nonce()
            padded = self._add_padding(plaintext)
            ciphertext = self.cipher.encrypt(nonce, padded, associated_data)
            self._increment_packet_count()
            return nonce + ciphertext  # prepend nonce for transmission

    def decrypt(self, data: bytes, associated_data: bytes = b'') -> bytes:
        with self._lock:
            nonce = data[:12]
            ciphertext = data[12:]
            plaintext_padded = self.cipher.decrypt(nonce, ciphertext, associated_data)
            plaintext = self._remove_padding(plaintext_padded)
            self._increment_packet_count()
            return plaintext

    def _generate_nonce(self) -> bytes:
        nonce = self.nonce_counter.to_bytes(12, byteorder='little')
        self.nonce_counter += 1
        return nonce

    def _add_padding(self, data: bytes) -> bytes:
        pad_len = os.urandom(1)[0] % 16  # random padding length 0-15 bytes
        return data + b'\x00' * pad_len

    def _remove_padding(self, data: bytes) -> bytes:
        return data.rstrip(b'\x00')

    def _increment_packet_count(self):
        self.packet_count += 1
        if self.packet_count >= self.KEY_ROTATION_THRESHOLD:
            self._rotate_keys()
            self.packet_count = 0

    def _rotate_keys(self):
        # For demonstration, generate new random keys (replace with HKDF from shared secret in real impl)
        self.encryption_key = os.urandom(32)
        self.mac_key = os.urandom(32)
        self.cipher = ChaCha20Poly1305(self.encryption_key)

    def zeroize(self):
        with self._lock:
            self.encryption_key = None
            self.mac_key = None
            self.cipher = None
