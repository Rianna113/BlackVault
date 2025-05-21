# Networking Module

## Overview

The Networking module manages secure message transport between BlackVault clients over TCP/IP or UDP.

Core responsibilities:

- Establish and maintain network connections with peers  
- Send and receive encrypted messages securely  
- Handle retransmissions, timeouts, and connection errors  
- Integrate with SessionManager to retrieve session keys for encryption

---

## Architecture

- Uses asynchronous sockets for scalable, non-blocking communication  
- Supports pluggable transport protocols (TCP, UDP)  
- Includes message framing and buffering for partial packets  
- Implements basic handshake messages to negotiate sessions before data exchange

---

## Usage Example

```python
from network.transport import TransportLayer

transport = TransportLayer()
transport.connect(peer_address)
transport.send_encrypted(peer_id, b'my secret message')
data = transport.receive()
