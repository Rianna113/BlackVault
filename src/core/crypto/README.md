# Crypto Primitives Module

## Overview

This module provides fundamental cryptographic operations and algorithms used by BlackVault’s higher-level modules.

Features include:

- Diffie-Hellman key exchange implementation  
- Key derivation functions (HKDF)  
- Digital signatures with ECDSA  
- Random number and key generation utilities

---

## Architecture

- Implements secure elliptic curve operations using PyCryptodome ECC  
- Provides high-level APIs for easy integration with Session Manager and Encryptor  
- Ensures cryptographic best practices and compliance with current standards

---

## Usage Example

```python
from crypto.diffie_hellman import DiffieHellman

dh = DiffieHellman()
public_key = dh.get_public_key()
shared_secret = dh.compute_shared_secret(peer_public_key)
