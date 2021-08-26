import socket 


HEADER = 64
PORT   = 2001
SERVER = socket.gethostbyname(socket.gethostname())
ADRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONECT'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADRESS)


def send(message):
    message = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2001).decode(FORMAT))

                                    
while True: 
    message = input('[MESSAGE] : ')
    if message.lower() == DISCONNECT_MESSAGE.lower():
        break
    else: 
        send(message)




