import socket
if __name__ == "__main__":
    client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address_udp = ('localhost', 5000)

    message = input("Enter a lowercase sentence: ")
    client_udp.sendto(message.encode(), server_address_udp)

    modified_message, server_address_udp = client_udp.recvfrom(1024)
    print("Modified Data from UDP Server:", modified_message.decode())

    client_udp.close()