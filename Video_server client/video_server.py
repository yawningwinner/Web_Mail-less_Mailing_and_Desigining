import cv2
import socket
import threading
import pickle
import struct
def handle_client(client_socket, addr):
    print(f'Connection from {addr}')
    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()
            data = pickle.dumps(frame)
            message_size = struct.pack("Q", len(data))
            client_socket.sendall(message_size + data)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cap.release()
        client_socket.close()
        print(f"Connection from {addr} closed")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 6969))
server_socket.listen(5)
print("Server listening on port 6969...")

while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
