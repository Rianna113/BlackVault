from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class Encryptor:
    def __init__(self, key: bytes):
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes for AES-256")
        self.key = key

    def encrypt(self, plaintext: bytes) -> tuple[bytes, bytes, bytes]:
        nonce = get_random_bytes(12)  # 96-bit nonce for GCM
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        return ciphertext, tag, nonce

    def decrypt(self, ciphertext: bytes, tag: bytes, nonce: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext
