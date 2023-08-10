import os
import signal
import socket


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Server:
    def __init__(self, host, port):
        # TODO:
        # 1. Define host and port
        # 2. Create a socket
        # 3. Bind the socket to the host and port
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

    def start(self):
        # TODO:
        # 1. Listen for incoming connections
        self.socket.listen()
        # print(f"Server listening on {self.host}:{self.port}")
        while True:
            # 2. Accept incoming connections
            conn, addr = self.socket.accept()
            # print(f"Connected by {addr}")

            # 3. Receive command and filename from client
            data = conn.recv(1024).decode()
            command, filename = data.split(" ")

            # 4. Check if the command is "download"
            if command != "download":
                # 4.1 If not, send an error message to the client: "Unknown command"
                # print(f'Unknown command: {command}')
                conn.sendall("Unknown command".encode())
                continue

            # print(f'Requested file: {filename}')

            # 5. Check if the file exists
            # 5.1 If not, send an error message to the client: "File doesn't exists"
            filepath = os.path.join(BASE_DIR, "files", filename)
            if not os.path.exists(filepath):
                # print(f'File not found: {filepath}')
                conn.sendall("File doesn't exists".encode())
                continue

            filesize = os.path.getsize(filepath)

            # 6. Send the header to the client
            # 6.1 Header format: "file-name: <filename>,\r\nfile-size: <filesize>\r\n\r\n"
            header = f"file-name: {filename},\r\nfile-size: {filesize}\r\n\r\n"
            print(header)
            conn.sendall(header.encode())

            # 7. Send the file to the client
            with open(filepath, "rb") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    conn.sendall(data)

            # 8. Close the connection
            conn.close()


def handler(signum, frame):
    raise Exception("end of time")


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(60)
    try:
        server = Server("127.0.0.1", 65432)
        server.start()
    except Exception as e:
        signal.alarm(0)
