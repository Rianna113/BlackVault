import unittest
from core.crypto.diffie_hellman import DiffieHellman

class TestDiffieHellman(unittest.TestCase):
    def test_key_generation(self):
        dh = DiffieHellman()
        pub_key = dh.get_public_key()
        self.assertIsInstance(pub_key, bytes)
        self.assertGreater(len(pub_key), 0)

    def test_shared_secret_agreement(self):
        alice = DiffieHellman()
        bob = DiffieHellman()

        alice_pub = alice.get_public_key()
        bob_pub = bob.get_public_key()

        alice_secret = alice.compute_shared_secret(bob_pub)
        bob_secret = bob.compute_shared_secret(alice_pub)

        self.assertEqual(alice_secret, bob_secret)

if __name__ == '__main__':
    unittest.main()
