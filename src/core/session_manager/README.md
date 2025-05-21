# Session Manager Module

## Overview

The Session Manager handles secure session establishment, key exchange, and lifecycle management for BlackVault communications.

Responsibilities include:

- Initiating and completing cryptographic handshakes using Diffie-Hellman key exchange  
- Generating and managing session keys with forward secrecy  
- Maintaining session states and timeouts  
- Supporting session resumption and renegotiation  
- Providing session-related metadata to other modules such as encryption and monitoring

---

## Architecture

- Central `SessionManager` class orchestrates handshake, key derivation, and session states  
- Supports asynchronous handshake operations  
- Uses cryptographic primitives from the `crypto` module

---

## Usage Example

```python
from session_manager import SessionManager

session_mgr = SessionManager()
session_mgr.start_handshake(peer_info)

# Use session_mgr to retrieve session keys and state
