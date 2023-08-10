from mocket import mocketize
import os
import socket

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SERVER_DIR = os.path.join(os.path.dirname(BASE_DIR), 'src/server')


@mocketize
def test_unknown():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 65432))

    # Send some data to the server
    conn.sendall('sample command'.encode())

    data = conn.recv(1024).decode()

    assert data == 'Unknown command'

    # Close the connection
    conn.close()
