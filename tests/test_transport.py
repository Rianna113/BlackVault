import unittest
import asyncio
from unittest.mock import AsyncMock, patch
from network.transport import TransportLayer

class TestTransportLayer(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = TransportLayer()
        self.transport.session_manager.get_session_key = AsyncMock(return_value=b'\x00' * 32)
        self.transport.logger = AsyncMock()

        # Mock connection (reader, writer)
        self.mock_writer = AsyncMock()
        self.mock_reader = AsyncMock()
        self.transport.connections['peer1'] = (self.mock_reader, self.mock_writer)

    @patch('network.transport.Encryptor')
    async def test_send_encrypted(self, mock_encryptor_cls):
        mock_encryptor = mock_encryptor_cls.return_value
        mock_encryptor.encrypt.return_value = (b'ciphertext', b'tag', b'nonce')

        await self.transport.send_encrypted('peer1', b'message')

        self.mock_writer.write.assert_called()
        self.mock_writer.drain.assert_awaited()
        self.transport.logger.info.assert_called()

    async def test_receive(self):
        # Prepare a fake message: length prefix + nonce+tag+ciphertext
        message = b'nonce12345678tagtagtagciphertextdata'
        length = len(message)
        self.mock_reader.readexactly = AsyncMock(side_effect=[length.to_bytes(4, 'big'), message])
        
        self.transport.session_manager.get_session_key = lambda peer_id: b'\x00' * 32
        
        # Patch Encryptor.decrypt to just return plaintext for testing
        with patch('network.transport.Encryptor.decrypt', return_value=b'plaintext'):
            plaintext = await self.transport.receive('peer1')

        self.assertEqual(plaintext, b'plaintext')

if __name__ == '__main__':
    unittest.main()
