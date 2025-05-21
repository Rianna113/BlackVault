# Encryption Module

## Overview

The Encryption module provides symmetric encryption and decryption capabilities for BlackVault, securing message confidentiality after key exchange.

Features include:

- AES-256 in GCM mode for authenticated encryption  
- Support for encryption and decryption of arbitrary data payloads  
- Secure generation and management of IVs (nonces)  
- Integration with Session Manager to use session keys transparently  
- Resistance to replay and tampering attacks through authentication tags

---

## Architecture

- Central `Encryptor` class exposes encrypt and decrypt methods  
- Uses cryptographic primitives from the Crypto module  
- Designed for performance and security, minimizing data copies and leaks

---

## Usage Example

```python
from encryption import Encryptor

encryptor = Encryptor(session_key)
ciphertext, tag, nonce = encryptor.encrypt(b"Secret Message")
plaintext = encryptor.decrypt(ciphertext, tag, nonce)
