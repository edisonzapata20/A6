import socket

HEADERSIZE = 10

# Define socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
s.connect((socket.gethostname(), int(values[1])))
while True:
    full_message = ''
    new_msg = True
    while True:
        # Accept message. Chunk of data to receive
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[: HEADERSIZE]}')
            msg_len = int(msg[: HEADERSIZE])
            new_msg = False

        full_message += msg.decode("utf-8")

        if len(full_message) - HEADERSIZE == msg_len:
            print("Full message received")
            print(full_message[HEADERSIZE:])
            new_msg = True
            full_message = ''

    print(full_message)
