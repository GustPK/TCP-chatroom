import socket
import threading

# Choosing Name
name = input("Enter your name: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 40847))

# Listening to Server and Sending Name
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NAME' Send Name
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(name, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()