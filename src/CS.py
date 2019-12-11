from _thread import *
import socket, time
import random


class CS(object):

    def __init__(self, msg):
        self.msg = msg
        self.possibleAnswers = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Dont count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.'
            'Very doubtful.'
        ]


    def main(self):
        serv = socket.socket()
        serv.bind((socket.gethostname(), 8888))
        # serv.bind(("localhost",8888))
        # serv.bind(("0.0.0.0",8888))
        # serv.bind(("",8888))
        serv.listen(10)
        start_new_thread(self.client, ())
        s, c = serv.accept()
        print("Message: " + s.recv(1024).decode("ASCII"))
        s.close()
        serv.close()

    def client(self):
        time.sleep(1)
        sock = socket.create_connection((socket.gethostname(), 8888))
        # sock=socket.create_connection(("localhost",8888))
        # Change from string to bytes
        my_str = random.choice(self.possibleAnswers)
        my_str_as_bytes = str.encode(my_str)
        type(my_str_as_bytes)

        sock.sendall(my_str_as_bytes)
        sock.close()
