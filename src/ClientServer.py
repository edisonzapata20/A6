import socket




def main():
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.connect((socket.gethostname(), 7777))

    msg = sockt.recv(1024)
    print(msg.decode("utf-8"))
