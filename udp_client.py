import socket


name = input('enter your username : ').strip()
bytesToSend1 = str.encode(name)
password = input('enter your password : ').strip()
bytesToSend2 = str.encode(password)

serverAddrPort = ("127.0.0.1", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)


UDPClientSocket.sendto(bytesToSend1, serverAddrPort)

UDPClientSocket.sendto(bytesToSend2, serverAddrPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0].decode())
print(msg)
