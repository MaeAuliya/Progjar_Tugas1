import socket
import select
import sys
import os

# IP SERVER dan PORT
IP = '127.0.0.1'
PORT = 5002

BUFFER_SIZE = 1024

server_address = (IP, PORT)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)        
            else:            	
                data = sock.recv(BUFFER_SIZE)
                
                if data:
                    # sock.send(data)
                    # data: teks string
                    data = data.decode()

                    # kalau perintah download dari client
                    if data.split()[0] == 'download':
                        print('masuk download')
                        # mencoba cari file
                        try:
                            # print(f'files/{data.split()[1]}')
                            f = open(f'files/{data.split()[1]}','r')
                            # file ada
                            if f:
                                print('tes')
                                # variabel untuk header
                                file_name = data.split()[1]
                                file_path = f'files/{data.split()[1]}'
                                file_size = int(os.path.getsize(file_path))

                                header = f'file-name: {file_name},\\n\nfile-size: {file_size},\\n\n\\n\\n'
                                
                                sock.send(f"{header}".encode())
                                with open(file_path, "rb") as f:
                                    while True:
                                        # read the bytes from the file
                                        bytes_read = f.read(BUFFER_SIZE)
                                        if not bytes_read:
                                            # file transmitting is done
                                            break
                                        # we use sendall to assure transimission in 
                                        # busy networks
                                        sock.sendall(bytes_read)
                                sock.close()
                        # file tidak ketemu
                        except OSError as e:
                            print('mohon maaf file tidak ada')
                    else:
                        print('Mohon maaf perintah tidak ditemukan')
                else:                    
                    sock.close()
                    input_socket.remove(sock)
except KeyboardInterrupt:        
    server_socket.close()
    sys.exit(0)