import ply.yacc as yac


def p_Server(p):
    '''
    Server :    NAME
              | UNDERSCORE
              | SPACE
              | NUMBER
    '''
    p[0] = p[1]


def p_ServerOperations(p):
    '''
    ServerOperations : UPDATE
                    | CONNECT
                    | DISCONNECT
                    | CREATE
                    | DELETE
    '''
    p[0] = p[1]

def p_ServerInteraction(p):
    '''

    ServerInteraction : ServerOperations Server

    '''
    p[0] = p[1]

def p_error(p):
    if p is not None:
        print ('Syntax error at line %s Error %s' % (p.lineno, p.value))
    else:
        print('Syntax error in input')

parser = yac.yacc()

while True:
    try:
        s = input('')   # use input() on Python 3
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)


#def p_ServerOperations(p):
    '''
  #  ServerOperations : UPDATE Server
   #                 | CONNECT Server
    #                | DISCONNECT Server
   #                 | CREATE Server
  #                  | DELETE Server
  #  '''
  #  p[0] = (p[2], [1])