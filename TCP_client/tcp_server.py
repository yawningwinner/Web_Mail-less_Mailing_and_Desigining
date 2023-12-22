import socket
if __name__ == "__main__":
    server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address_tcp = ('localhost', 6000)
    server_tcp.bind(server_address_tcp)
    server_tcp.listen()

    print("TCP Server is waiting for a connection...")
    
    client_tcp, client_address_tcp = server_tcp.accept()
    data = client_tcp.recv(1024)
    modified_data = data.decode().upper()
    client_tcp.sendall(modified_data.encode())

    client_tcp.close()
