from _thread import *
import socket, time


def client():
    # print("Thread starts")
    time.sleep(1)
    # print("Thread connects")
    sock = socket.create_connection((socket.gethostname(), 8888))
    # sock=socket.create_connection(("localhost",8888))
    # print("Thread after connect")
    sock.sendall(b"Hello from client")
    sock.close()
    # print("Thread ends")


def main(msg):
    serv = socket.socket()
    serv.bind((socket.gethostname(), 8888))
    # serv.bind(("localhost",8888))
    # serv.bind(("0.0.0.0",8888))
    # serv.bind(("",8888))
    serv.listen(10)
    start_new_thread(client, ())
    # print("Before accept")
    s, c = serv.accept()
    # print("After accept " + c[ 0 ])
    print("Message: " + s.recv(1024).decode("ASCII"))
    s.close()
    serv.close()


if __name__ == '__main__':
    main()

