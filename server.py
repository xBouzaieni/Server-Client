import socket
import threading 
from tqdm import tqdm
from time import sleep

HEADER = 64
PORT   = 2001
SERVER = socket.gethostbyname(socket.gethostname())
ADRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADRESS)



def handle_client(connection, adress):
    print(f'[NEW CONNECTION] {adress} connected')
    connected = True 
    while connected: 
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False 
                print(f'[CLIENT - {adress}] has disconnected')
            print(f'[{adress}] : {message}')
            connection.send('[NOTIFICATION] : Mr. SERVER got your message'.encode(FORMAT))
    connection.close()



def start():
    server.listen()
    print(f'[LISTENING] server is listening on {SERVER}')
    while True: 
        connection , adress = server.accept()
        thread = threading.Thread(target = handle_client, args = (connection, adress))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 2}')



pbar = tqdm(["", "", "", ""])
for char in pbar:
    sleep(0.25)
    pbar.set_description("[STARTING] %s" % char)

start()
