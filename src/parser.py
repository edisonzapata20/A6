import ply.yacc as yacc
import ClientServer
import lexer
import mserver
import mclient
import yanise

tokens = lexer.tokens

from lexer import help

a = []


def p_ServerAssign_Connection(p):
    """ServerAssign_Connection : CONNECT SPACE NAME
                    | DISCONNECT SPACE NAME
    """

    if p[1] == "Connect":
        a.append(p[3])
        print("Server" + " " + p[3] + " " + "running")
        yanise.main()
    if p[1] == "Disconnect" and len(a) != 0 and a[0] == p[3]:
        a.remove(a[0])
        print("Server" + " " + p[3] + " " + "disconnected")
    elif p[1] == "Disconnect" and len(a) == 0:
        print("There is no running server.")


def p_error(p):
    print("Syntax error! Command should be 'Connect/Disconnect servername' ")


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
