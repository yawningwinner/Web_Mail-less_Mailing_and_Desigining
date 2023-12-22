import socket
if __name__ == "__main__":
    server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address_udp = ('localhost', 5000)
    server_udp.bind(server_address_udp)

    while True:
        print("UDP Server is waiting for a message...")
        data, client_address = server_udp.recvfrom(1024)
        modified_data = data.decode().upper()
        server_udp.sendto(modified_data.encode(), client_address)