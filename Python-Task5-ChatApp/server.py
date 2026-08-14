import socket
import threading
from datetime import datetime

# Connection Data
HOST = '127.0.0.1' # Localhost
PORT = 5555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

def broadcast(message):
    """Sends a message to all connected clients."""
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle_client(client):
    """Handles incoming messages from a specific client."""
    while True:
        try:
            # Receive message from client
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
                
            # Add timestamp prefix (e.g., [14:35] Alice: Hello)
            now = datetime.now().strftime("%H:%M")
            formatted_message = f"[{now}] {message}"
            
            # Broadcast to everyone
            print(formatted_message) # Print on server console too
            broadcast(formatted_message.encode('utf-8'))
        except:
            break
            
    # Graceful Disconnection Handling
    index = clients.index(client)
    clients.remove(client)
    client.close()
    
    username = usernames[index]
    usernames.remove(username)
    
    now = datetime.now().strftime("%H:%M")
    disconnect_msg = f"[{now}] Server: {username} has left the chat."
    print(disconnect_msg)
    broadcast(disconnect_msg.encode('utf-8'))

def receive():
    """Accepts new connections."""
    print(f"Server is listening on {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        
        # Request and store username
        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)
        
        print(f"Connection established with {str(address)} | Username: {username}")
        
        # Announce new user
        now = datetime.now().strftime("%H:%M")
        join_msg = f"[{now}] Server: {username} joined the chat!"
        broadcast(join_msg.encode('utf-8'))
        client.send(f"[{now}] Server: Connected to the server successfully!".encode('utf-8'))
        
        # Start a thread to listen to this client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
