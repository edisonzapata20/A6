import ply.yacc as yacc
import ClientServer
import lexer
tokens = lexer.tokens

from lexer import help



def p_ServerName(p):

    """ServerName : CONNECT SPACE NAME
                    | DISCONNECT SPACE NAME
    """


    print(p[3])
    a = p[3]
    if p[1] == "Connect":
        ClientServer.main()
        print('Server running')
    if p[1] == "Disconnect" and p[3] == a:
        print("Server disconnected")



def p_error(p):
    if p:
        print ('Syntax error at line %s Error %s' % (p.lineno, p.value))
    else:
        print('Syntax error in input')


parser = yacc.yacc()

while True:
    try:
        s = input('ServerCommunication>')
    except EOFError:
        break
    if not s: continue
    if (s == 'help'):
        help()
        continue
    result = parser.parse(s)


