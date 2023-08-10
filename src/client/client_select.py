import socket
import tqdm
import sys

# IP SERVER dan PORT
IP = '127.0.0.1'
PORT = 5002
BUFFER_SIZE = 1024

server_address = (IP, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

def parsing_header(header):
    info = header.split(',\\n')
    file_name = info[0].split()
    file_name = file_name[1]
    file_size = info[1]
    file_size = file_size[1:].split()
    file_size = file_size[1]
    print(file_name) 
    print(file_size)

    return file_name, file_size

try:
    while True:
        message = sys.stdin.readline()
        client_socket.send(bytes(message, 'utf-8'))
        # menerima header
        # header_data = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        received_data = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        # sys.stdout.write(received_data)
        file_name, file_size = parsing_header(received_data)

        print(file_name)
        with open(file_name, 'wb+') as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)

except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)