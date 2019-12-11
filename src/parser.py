import ply.yacc as yacc
import lexer
import yanise

tokens = lexer.tokens

from lexer import help



def p_ServerAssign_Connection(p):
    """ServerAssign_Connection : CONNECT SPACE TO SPACE SERVER SPACE NAME
                    | DISCONNECT SPACE SERVER NAME
    """

    if p[1] == "Connect":
        print("Server" + " " + p[7] + " " + "running")
        yanise.main()



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
