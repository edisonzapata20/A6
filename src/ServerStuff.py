import socket



sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.bind((socket.gethostname(), 7777))
sockt.listen(5)

while True:
        clientsocket, address = sockt.accept()
        print(f"Connection from {address} established!")
        clientsocket.send(bytes("Server has been accessed","utf-8"))

def close():
    clientsocket.close()