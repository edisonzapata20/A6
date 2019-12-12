import ply.lex as lexer

def help():
    print("Welcome to CSFlow, a programming language to simplify communication between devices.\n")
    print('''To connect to a server type 'Connect to Server SERVERNAME' 
    ''')
    print("Then, type a question ending in '?' to ask the server.")
    print("To close program, type 'Disconnect'.")


tokens = [
    'NAME',
    'SPACE',
    'CONNECT',
    'SERVER',
    'TO',
    'DISCONNECT'
]

t_SPACE = r'\ '


def t_TO(t):
    r'to'
    t.type = 'TO'
    return t

def t_CONNECT(t):
    r'Connect'
    t.type = 'CONNECT'
    return t

def t_DISCONNECT(t):
    r'Disconnect'
    t.type = 'DISCONNECT'
    return t

def t_SERVER(t):
    r'Server'
    t.type = 'SERVER'
    return t

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t



def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


lex = lexer.lex()


# To test Lexer
#lexer.input("Connect=a2")

#while True:
   # tok = lexer.token()
   # if not tok:
   #   break
  #  print(tok)