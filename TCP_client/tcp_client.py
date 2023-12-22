import socket
if __name__ == "__main__":
    client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address_tcp = ('localhost', 6000)

    client_tcp.connect(server_address_tcp)
    message = input("Enter a lowercase sentence: ")
    client_tcp.sendall(message.encode())

    modified_message = client_tcp.recv(1024)
    print("Modified Data from TCP Server:", modified_message.decode())

    client_tcp.close()
