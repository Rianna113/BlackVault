# Crypto Module

## Overview

The Crypto module provides fundamental cryptographic primitives for BlackVault's secure communication framework.

Features include:

- Diffie-Hellman key exchange implementation for secure shared secret generation  
- Symmetric encryption and decryption primitives  
- Secure random number generation  
- Hashing utilities for key derivation and message integrity  
- Interfaces designed for easy integration with session management and encryption modules

---

## Architecture

- Contains classes and functions for core crypto algorithms  
- Designed with security best practices and constant-time operations where applicable  
- Easily extendable to support additional algorithms or hardware acceleration

---

## Usage Example

```python
from crypto import DiffieHellman

dh = DiffieHellman()
pub_key = dh.get_public_key()
shared_secret = dh.compute_shared_secret(peer_pub_key)
