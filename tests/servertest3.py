from mocket import mocketize
import os
import socket

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SERVER_DIR = os.path.join(os.path.dirname(BASE_DIR), 'src/server')


@mocketize
def test_first_file():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 65432))

    # Send some data to the server
    conn.sendall('download 729.txt'.encode())

    header = conn.recv(42).decode()

    assert 'file-name: 729.txt,\r\nfile-size: 109513\r\n\r\n' in header

    data = b''
    while True:
        try:
            data = data + conn.recv(1024)
            if not data:
                break
        except BlockingIOError:
            break

    with open(os.path.join(SERVER_DIR, 'files', '729.txt'), 'rb') as f:
        assert data == f.read()

    # Close the connection
    conn.close()


@mocketize
def test_second_file():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 65432))

    # Send some data to the server
    conn.sendall('download s41066-020-00226-2.pdf'.encode())

    header = conn.recv(58).decode()

    assert 'file-name: s41066-020-00226-2.pdf,\r\nfile-size: 1191710\r\n\r\n' in header

    data = b''
    while True:
        try:
            data = data + conn.recv(1024)
            if not data:
                break
        except BlockingIOError:
            break

    with open(os.path.join(SERVER_DIR, 'files', 's41066-020-00226-2.pdf'), 'rb') as f:
        assert data == f.read()

    # Close the connection
    conn.close()


@mocketize
def test_third_file():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 65432))

    # Send some data to the server
    conn.sendall('download xlsx.zip'.encode())

    header = conn.recv(44).decode()

    assert 'file-name: xlsx.zip,\r\nfile-size: 5702506\r\n\r\n' in header

    data = b''
    while True:
        try:
            data = data + conn.recv(1024)
            if not data:
                break
        except BlockingIOError:
            break

    with open(os.path.join(SERVER_DIR, 'files', 'xlsx.zip'), 'rb') as f:
        assert data == f.read()

    # Close the connection
    conn.close()
