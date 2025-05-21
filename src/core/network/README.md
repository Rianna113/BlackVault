# Network Module

## Overview

The Network module manages secure transmission and reception of encrypted messages between BlackVault peers.

Features include:

- TCP/UDP socket management for reliable data transfer  
- Message framing and protocol encoding/decoding  
- Integration with Session Manager to fetch session keys for encryption/decryption  
- Detection and handling of network errors and timeouts  
- Supports message retransmission and order preservation where applicable

---

## Architecture

- `NetworkManager` class abstracts socket operations and protocol logic  
- Uses asynchronous I/O to maximize throughput and responsiveness  
- Interfaces cleanly with core encryption and session modules

---

## Usage Example

```python
from network import NetworkManager

network = NetworkManager()
network.send_message(peer_id, plaintext_message)
received = network.receive_message()
