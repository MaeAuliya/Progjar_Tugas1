import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.client.client_serversocket import Client

class TestClient(unittest.TestCase):
    @patch('src.client.client_serversocket.Client.send_message')
    def test_attribute1(self, mock_send_message):
        mock_send_message.return_value = "file-name: test.txt, file-size: 100"
        client = Client("localhost", 65432)
        test = client.send_message("test")
        file_name, file_size = client.parse_header(test)
        assert file_name == "test.txt"
        assert file_size == 100

    

