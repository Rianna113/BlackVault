import secrets

class DiffieHellman:
    # Using 2048-bit MODP Group from RFC 3526 (Group 14)
    _prime = int(
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08"
        "8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD"
        "3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A36210000000000090563", 16
    )
    _generator = 2

    def __init__(self):
        self._private_key = secrets.randbelow(self._prime - 2) + 1
        self._public_key = pow(self._generator, self._private_key, self._prime)

    def get_public_key(self) -> bytes:
        return self._public_key.to_bytes((self._public_key.bit_length() + 7) // 8, byteorder='big')

    def compute_shared_secret(self, peer_public_bytes: bytes) -> bytes:
        peer_public_key = int.from_bytes(peer_public_bytes, byteorder='big')
        if not (1 < peer_public_key < self._prime - 1):
            raise ValueError("Invalid peer public key")
        shared_secret = pow(peer_public_key, self._private_key, self._prime)
        return shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, byteorder='big')
