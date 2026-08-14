import socket
import threading
import sys

username = input("Choose your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1', 5555))
except ConnectionRefusedError:
    print("Error: Could not connect. Is server.py running?")
    sys.exit()

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        try:
            message = f'{username}: {input("")}'
            client.send(message.encode('utf-8'))
        except:
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
