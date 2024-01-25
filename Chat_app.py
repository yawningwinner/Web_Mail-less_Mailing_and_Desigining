import socket
import threading
import os

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind(("192.168.29.81",2024))
nm = input("ENTER YOUR NAME : ")
print("\nType 'quit' to exit.")

ip,port = input("Enter IP address and Port number: ").split()

def send():
    while True:
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , (ip,int(port)))

def rec():
    while True:
        msg = s.recvfrom(1024)
        print("message from device : >> " +  msg[0].decode()  )
        print(">> ")
t1 = threading.Thread( target = send )
t2 = threading.Thread( target = rec )

t1.start()
t2.start()
