import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Server's IP address (local)
PORT = 12345        # Must match the server's port

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print("\n" + message)
            else:
                break
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to the server. Start typing your messages.")

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(client,)).start()

    # Main loop to send messages
    while True:
        message = input()
        if message.lower() == 'exit':
            client.send('User has left the chat.'.encode('utf-8'))
            break
        client.send(message.encode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()

