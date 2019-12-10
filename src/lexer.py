import ply.lex as lexer
import ply.yacc as yac



def help():
    print('''Server PL
    ''')


tokens = [
    'NAME',
    'SPACE',
    'CONNECT',
    'DISCONNECT'

]

t_SPACE = r'\ '



#def t_NUMBER(t):
   # r'\d+'
   # t.value = int(t.value)
    #return t

def t_CONNECT(t):
    r'Connect'
    t.type = 'CONNECT'
    return t


def t_DISCONNECT(t):
    r'Disconnect'
    t.type = 'DISCONNECT'
    return t

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t



def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


lex = lexer.lex()


#For testing lexer
#lexer.input("Connect")

#while True:
   # tok = lexer.token()
   # if not tok:
    #    break
   # print(tok)
