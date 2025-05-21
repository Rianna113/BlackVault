from Crypto.PublicKey import ECC

class DiffieHellman:
    def __init__(self):
        self._private_key = ECC.generate(curve='P-256')
        self._public_key = self._private_key.public_key()

    def get_public_key(self):
        return self._public_key.export_key(format='DER')

    def compute_shared_secret(self, peer_public_bytes):
        peer_public_key = ECC.import_key(peer_public_bytes)
        shared_point = self._private_key.d * peer_public_key.pointQ
        shared_secret = int(shared_point.x).to_bytes(32, byteorder='big')
        return shared_secret
