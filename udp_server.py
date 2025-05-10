import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

di ={'ilknur': 'ebru', 'buse':'tuçe', 'burak':'bedirhan',
'17BCE2119':'sahil', '17BIT0123':'sidhant'}


while True:
    try:

        name, addr1 = UDPServerSocket.recvfrom(bufferSize)

        pwd, addr1 = UDPServerSocket.recvfrom(bufferSize)

        name = name.decode().strip()
        pwd = pwd.decode().strip()

        # Kontrol et
        if name not in di:
            msg = 'name does not exist'
        elif di[name] == pwd:
            msg = 'pwd match'
        else:
            msg = 'pwd wrong'


        bytesToSend = msg.encode()
        UDPServerSocket.sendto(bytesToSend, addr1)

    except Exception as e:
        print("Sunucuda hata oluştu:", e)
