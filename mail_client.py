from socket import *
from base64 import *
import ssl
#User Details
userEmail = input("Enter Your Email Address: ")
userPassword = input("Enter Your Password: ")
userDestinationEmail = input("Enter Email Destination: ")
userSubject = input("Enter Subject: ")
userBody = input("Enter Message: ")
msg = '{}.\r\n Try not to know me'.format(userBody)
endmsg = "\r\n.\r\n"
# Server Crendentials
mailserver = 'mmtp.iitk.ac.in'
mailPort = 25
#Connect
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))
recv = clientSocket.recv(1024).decode()
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
clientSocket.recv(1024)
sslClientSocket = ssl.wrap_socket(clientSocket)
#Authenticate and connect, then send the required info
authorizationCMD = "AUTH LOGIN\r\n"
sslClientSocket.send(authorizationCMD.encode())
email = b64encode(userEmail.encode()).decode()
Passoword = b64encode(userPassword.encode()).decode()
sslClientSocket.send((email + "\r\n").encode())
sslClientSocket.send((Passoword + "\r\n").encode())
mailFrom = "Mail from: <{}>\r\n".format(userEmail)
sslClientSocket.send(mailFrom.encode())
rcptto = "RCPT TO: <{}>\r\n".format(userDestinationEmail)
sslClientSocket.send(rcptto.encode())
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
sslClientSocket.send("Subject: {}\n\n{}".format(userSubject, msg).encode())
sslClientSocket.send(endmsg.encode())
quitCMD = 'QUIT\r\n'
sslClientSocket.send(quitCMD.encode())
sslClientSocket.close()
print('Success') 
