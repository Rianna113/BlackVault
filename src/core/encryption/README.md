# Encryptor Module

## Overview

The Encryptor module provides authenticated encryption and decryption using AES-GCM, ensuring confidentiality and integrity for BlackVault messages.

Features:

- AES-GCM encryption with 256-bit keys  
- Generates secure random nonces for each encryption  
- Supports encrypting arbitrary byte messages  
- Verifies message authenticity on decryption and raises errors on tampering

---

## Architecture

- Uses PyCryptodome’s AES-GCM implementation  
- Integrates seamlessly with SessionManager for key retrieval  
- Provides simple `encrypt` and `decrypt` APIs returning ciphertext, tag, and nonce

---

## Usage Example

```python
from encryption.encryptor import Encryptor

key = b'\x00' * 32  # Replace with session key
encryptor = Encryptor(key)
ciphertext, tag, nonce = encryptor.encrypt(b'secret message')
plaintext = encryptor.decrypt(ciphertext, tag, nonce)
