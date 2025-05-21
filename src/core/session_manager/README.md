# Session Manager Module

## Overview

The Session Manager module handles establishing, maintaining, and terminating secure communication sessions between BlackVault peers.

Core responsibilities:

- Perform key exchange handshake (Diffie-Hellman)  
- Manage session keys lifecycle (generation, storage, expiration)  
- Provide session keys to encryption and network modules  
- Detect and recover from session failures  
- Ensure forward secrecy by rotating keys periodically

---

## Architecture

- Central `SessionManager` class exposes API to start and manage sessions  
- Uses Diffie-Hellman from crypto module for secure key agreement  
- Stores session state in-memory with optional persistent backing

---

## Usage Example

```python
from session_manager import SessionManager

sm = SessionManager()
sm.initiate_session(peer_id)
key = sm.get_session_key(peer_id)
