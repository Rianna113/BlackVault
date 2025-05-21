# Handshake Engine Module

## Overview

This module implements the ephemeral key exchange and session authentication process as defined in the BlackVault protocol specification (`/docs/02_PROTOCOL_SPEC.md`).

Key responsibilities include:

- Generating ephemeral X25519 key pairs for client and server  
- Performing Diffie-Hellman shared secret computation  
- Deriving session keys using HKDF-SHA256  
- Managing session lifecycle and timeouts  
- Authenticating sessions with Ed25519 signatures  
- Detecting anomalies and triggering early kill-switch if needed

## Architecture

- `HandshakeEngine` class encapsulates handshake logic  
- Separate classes for Client and Server handshake roles  
- Clear interfaces for integration with networking layers  
- Asynchronous event-driven design for non-blocking handshake processing

## Usage

```python
from handshake_engine import HandshakeEngine

engine = HandshakeEngine(role='client')
engine.start_handshake(peer_public_key)

# Await completion event
if engine.is_handshake_complete():
    session_keys = engine.get_session_keys()
else:
    # Handle handshake failure or timeout

Security Notes
All private keys are zeroed out after use

Strict timing constraints to prevent replay attacks

Early abort triggers kill switch if handshake messages are malformed or delayed excessively

Testing
Unit tests cover key generation, shared secret computation, and timeout behavior

Fuzz tests simulate corrupted handshake messages and network anomalies

By anchoring session security in this engine, BlackVault ensures every connection is a fortress from the start.
