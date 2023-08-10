from mocket import mocketize
import os
import socket
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from src.client.client_serversocket import Client


@mocketize
def test_attribute1():
    client = Client("localhost", 65432)
    assert client.host == "localhost"
    assert client.port == 65432


@mocketize
def test_attribute2():
    client = Client("127.0.0.1", 65432)
    assert client.host == "127.0.0.1"
    assert client.port == 65432


@mocketize
def test_attribute3():
    client = Client("localhost", 5000)
    assert client.host == "localhost"
    assert client.port == 5000


@mocketize
def test_attribute4():
    client = Client("127.0.0.1", 5000)
    assert client.host == "127.0.0.1"
    assert client.port == 5000
