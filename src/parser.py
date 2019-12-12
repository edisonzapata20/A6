import sys

import ply.yacc as yacc
import lexer
import CS

tokens = lexer.tokens
msg = ""

from lexer import help

def p_ServerAssign_Connection(p):
    """ServerAssign_Connection : CONNECT SPACE TO SPACE SERVER SPACE NAME
                                | DISCONNECT
    """

    if p[1] == "Connect":
        msg = input("Ask the server a question> ")

        if len(msg) != 0 and msg[len(msg) - 1] == '?':
            print("Server" + " " + p[7] + " " + "running")
            cs = CS.CS(msg)
            cs.main()
        else:
            print("Invalid or empty message. Message must be a question ending in '?'")
    elif p[1] == "Disconnect":
        sys.exit()

def p_error(p):
    print("Syntax error! Command should be 'Connect to Server servername' ")


parser = yacc.yacc()

while True:
    try:
        s = input("ServerCommunication (Type 'help' for assistance)>")
    except EOFError:
        break
    if not s: continue
    if s == 'help':
        help()
        continue
    result = parser.parse(s)