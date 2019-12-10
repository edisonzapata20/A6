import socket
import time

HEADERSIZE = 10

# Define socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind of socket with IP and port
s.bind((socket.gethostname(), 7777))
# Prepares for message
s.listen(5)

# Listen forever for a connection
while True:
    # If connection got, accept it
    # clientsocket -> object del socket del client
    # address -> where they are coming from (IP)
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    # String formatting
    msg = "Welcome to the server."
    # Length of message
    msg = f'{len(msg) :< {HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f'{len(msg) :< {HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
