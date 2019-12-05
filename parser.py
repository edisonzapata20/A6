import ply.yacc as yac

from lexer import lexer

def p_serverName(p):
    'serverName: LETTER NUMBER'
    p[0] = p[2]


def p_errors(p):
    if p is not None:
        print ('Syntax error at line %s Error %s' % (p.lineno, p.value))
    else:
        print('Syntax error in input')


parser = yac.yacc()

