import cv2
import socket
import pickle
import struct
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 6969))
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) #to display the recieved frame
try:
    while True:
        data = b""
        payload_size = struct.calcsize("Q")
        while len(data) < payload_size:
            data += client_socket.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        print("dikhaa shakal")
        cv2.imshow("Live Video Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cv2.destroyAllWindows()
    client_socket.close()
