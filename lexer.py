import ply.lex as lexer


keywords = {
    'connect': 'CONNECT',
    'disconnect': 'DISCONNECT',
    'create_server': 'CREATE_SERVER',
    'delete_server': 'DELETE_SERVER',
    'update_server': 'UPDATE_SERVER',
}

tokens = (
    'Letter',
    'Number',


)

def t_Number(t):
    r'\N+'
    t.value = int(t.value)
    return t

def t_Letter(t):
    r'[a-zA-Z]'
    t.type = keywords.get(t.value, "Letter")



lex = lexer.lex()