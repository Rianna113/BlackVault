import unittest
from core.session_manager.session_manager import SessionManager

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        self.session_manager = SessionManager()

    def test_create_and_get_session_key(self):
        peer_id = 'peer1'
        key = self.session_manager.create_session_key(peer_id)
        self.assertEqual(len(key), 32)
        retrieved_key = self.session_manager.get_session_key(peer_id)
        self.assertEqual(key, retrieved_key)

    def test_remove_session_key(self):
        peer_id = 'peer1'
        self.session_manager.create_session_key(peer_id)
        self.session_manager.remove_session_key(peer_id)
        self.assertIsNone(self.session_manager.get_session_key(peer_id))

if __name__ == '__main__':
    unittest.main()
