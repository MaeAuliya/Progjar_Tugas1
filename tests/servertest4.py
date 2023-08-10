from mocket import mocketize
import os
import socket
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SERVER_DIR = os.path.join(os.path.dirname(BASE_DIR), 'src/server')
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from src.server.server_serversocket import Server

@mocketize
def test_attribute():
    server = Server("localhost", 65432)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    assert server.host == "localhost"
    assert server.port == 65432
    assert type(server.socket) == type(sock)


@mocketize
def test_attribute2():
    server = Server("localhost", 5000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    assert server.host == "localhost"
    assert server.port == 5000
    assert type(server.socket) == type(sock)


@mocketize
def test_attribute3():
    server = Server("127.0.0.1", 65432)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    assert server.host == "127.0.0.1"
    assert server.port == 65432
    assert type(server.socket) == type(sock)


@mocketize
def test_attribute4():
    server = Server("127.0.0.1", 8000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    assert server.host == "127.0.0.1"
    assert server.port == 8000
    assert type(server.socket) == type(sock)
