import unittest
from core.encryption.encryptor import Encryptor

class TestEncryptor(unittest.TestCase):
    def setUp(self):
        self.key = b'\x00' * 32
        self.encryptor = Encryptor(self.key)

    def test_encrypt_decrypt(self):
        plaintext = b"test message"
        ciphertext, tag, nonce = self.encryptor.encrypt(plaintext)
        decrypted = self.encryptor.decrypt(ciphertext, tag, nonce)
        self.assertEqual(decrypted, plaintext)

    def test_tamper_detection(self):
        plaintext = b"test message"
        ciphertext, tag, nonce = self.encryptor.encrypt(plaintext)
        tampered_ciphertext = ciphertext[:-1] + bytes([ciphertext[-1] ^ 0x01])
        with self.assertRaises(Exception):
            self.encryptor.decrypt(tampered_ciphertext, tag, nonce)

if __name__ == '__main__':
    unittest.main()
