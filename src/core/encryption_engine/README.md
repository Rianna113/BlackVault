# Encryption Engine Module

## Overview

The Encryption Engine handles all cryptographic operations related to encrypting and decrypting BlackVault’s communication payloads.

It ensures:

- **Confidentiality:** Using ChaCha20-Poly1305 AEAD for authenticated encryption  
- **Integrity:** Message authentication codes (MACs) verify payload authenticity  
- **Replay Protection:** Incorporates nonces and sequence numbers  
- **Key Management:** Works with session keys derived during handshake  
- **Padding:** Implements randomized padding to obscure message length and patterns

---

## Architecture

- `EncryptionEngine` class encapsulates encryption and decryption logic  
- Supports both streaming and discrete message encryption  
- Uses cryptography library primitives for cipher and MAC  
- Designed for thread-safe concurrent operation

---

## Usage Example

```python
from encryption_engine import EncryptionEngine

engine = EncryptionEngine(session_keys)
ciphertext, mac = engine.encrypt(plaintext, nonce)
plaintext = engine.decrypt(ciphertext, nonce, mac)
