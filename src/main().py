import mylexer
import myparser
import socket

HEADERSIZE = 10
values = []
def main():

    #Read the current flow source code in test.lang and store it in a variable
    content = ""
    # test.lang -> snippet of language syntax
    # 'r' -> read only
    with open('CSFlow.lang', 'r') as file:
        content = file.read()

    #Lexer
    #instance of the Lexer class y le mandamos content al "constructor"
    lex = mylexer.Lexer(content)
    #call tokenize()
    tokens = lex.tokenize

    #Parser
    # instance of the Parser class y le mandamos tokens al "constructor"
    parse = myparser.Parser(tokens)
    valueArr = parse.parse()

    for i in valueArr:
        if len(i) != 0:
            values.append(i)

main()

# ------------------------------Client------------------------
# Define socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
s.connect((values[0], int(values[1])))

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


