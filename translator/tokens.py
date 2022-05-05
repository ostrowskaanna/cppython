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
    'unsigned': 'UNSIGNED',
    'double': 'DOUBLE',
    'class': 'CLASS',
    'break': 'BREAK',
    'switch': 'SWITCH',
    'case': 'CASE',
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


t_ignore = ' '


def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')    # Check for reserved words if not in reserved words than its VAR
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

with open('TestInput\input2') as f:
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

