from mocket import mocketize
import os
import socket

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SERVER_DIR = os.path.join(os.path.dirname(BASE_DIR), 'src/server')


@mocketize
def test_not_exists():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 65432))

    # Send some data to the server
    conn.sendall('download sample.txt'.encode())

    data = conn.recv(1024).decode()

    assert data == "File doesn't exists"

    # Close the connection
    conn.close()
