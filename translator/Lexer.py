from ply import lex
from ply import yacc


reserved = {
    'for': 'FOR',
    'while': 'WHILE',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'int': 'INT',
    'char': 'CHAR',
    'string': 'STRING',
    'bool': 'BOOL',
    'float': 'FLOAT',
    'long': 'LONG',
    'short': 'SHORT',
    'double': 'DOUBLE',
    'class': 'CLASS',
    'break': 'BREAK',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'include': 'INCLUDE',
    'using': 'USING',
    'namespace': 'NAMESPACE',
    'std': 'STD',
    'void': 'VOID',
    'endl': 'ENDL'
}

tokens = [
    # operators and signs
    'COMMENT',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'EQUAL_EQUAL',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'EQUAL',
    'LEFT_BR',
    'RIGHT_BR',
    'LEFT_BR_SQUARED',
    'RIGHT_BR_SQUARED',
    'LEFT_BR_CURLY',
    'RIGHT_BR_CURLY',
    'SEMICOLON',
    'COLON',
    'LESS',
    'LESS_EQUAL',
    'GREATER',
    'GREATER_EQUAL',
    'NOT_EQUAL',
    'HASH',
    # numbers and variables
    'INT_NUMBER',
    'FLOAT_NUMBER',
    'VAR',
    # ID for keywords
    'ID'
] + list(reserved.values())


def t_comment(t):
    r'\//.*'
    pass
    # No return value. Token discarded


t_PLUS_PLUS = r'\++'
t_MINUS_MINUS = r'--'
t_EQUAL_EQUAL = r'=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUAL = r'\='
t_LEFT_BR = r'\('
t_RIGHT_BR = r'\)'
t_LEFT_BR_SQUARED = r'\['
t_RIGHT_BR_SQUARED = r'\]'
t_LEFT_BR_CURLY = r'\{'
t_RIGHT_BR_CURLY = r'\}'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_LESS = r'\<'
t_LESS_EQUAL = r'\<='
t_GREATER = r'\>'
t_GREATER_EQUAL = r'\>='
t_NOT_EQUAL = r'\!='
t_HASH = r'\#'

t_ignore = ' '


def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')    # Check for reserved words if not in reserved words than its VAR
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


with open('TestInput\input') as f:
    lines = f.readlines()

code = "".join(lines)

lexer = lex.lex()

lexer.input(code)

while True:
    tok = lexer.token()
    if not tok:
        break
    else:
        print(tok)






# wersja z parowaniem nawiasy
# def t_LEFT_BR(t):
#     r'\('
#     t.type = 'LEFT_BR'
#     t.lexer.br_count = 1
#     return t
#
# def t_RIGHT_BR(t):
#     r'\)'
#     if t.lexer.br_count == 1:
#         t.type = 'RIGHT_BR'
#         t.lexer.br_count = 0
#         return t
#     else:
#         print("No opening bracket for ')'")
#
# def t_LEFT_BR_SQUARED(t):
#     r'\['
#     t.type = 'LEFT_BR_SQUARED'
#     t.lexer.br_squared_count = 1
#     return t
#
# def t_RIGHT_BR_SQUARED(t):
#     r'\]'
#     if t.lexer.br_squared_count == 1:
#         t.type = 'RIGHT_BR_SQUARED'
#         t.lexer.br_squared_count = 0
#         return t
#     else:
#         print("No opening bracket for ']'")
#
# def t_LEFT_BR_CURLY(t):
#     r'\{'
#     t.type = 'LEFT_BR_CURLY'
#     t.lexer.br_curly_count = 1
#     return t
#
# def t_RIGHT_BR_CURLY(t):
#     r'\}'
#     if t.lexer.br_curly_count == 1:
#         t.type = 'RIGHT_BR_CURLY'
#         t.lexer.br_curly_count = 0
#         return t
#     else:
#         print("No opening bracket for '}'")

