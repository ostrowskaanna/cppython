from ply import lex
from ply import yacc


tokens = [

    'FOR',
    'WHILE',
    'PUBLIC',
    'PRIVATE',
    'PROTECTED',
    'INT',
    'CHAR',
    'STRING',
    'BOOL',
    'FLOAT',
    'LONG',
    'SHORT',
    'UNSIGNED',
    'DOUBLE',
    'CLASS',
    'BREAK',
    'SWITCH',
    'CASE',
    'IF',
    'ELSE',
    'RETURN',
    'TRUE',
    'FALSE',
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'VOID',

    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'EQUAL',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'EQUAL_EQUAL',
    'LEFT_BR',
    'RIGHT_BR',
    'LEFT_BR_SQUARED',
    'RIGHT_BR_SQUARED',
    'LEFT_BR_CURLY',
    'RIGHT_BR_CURLY',

    'NUMBER',
    'VAR'

]

t_FOR = 'for'
t_WHILE = 'while'
t_PUBLIC = 'public'
t_PRIVATE = 'private'
t_PROTECTED = 'protected'
t_INT = 'int'
t_CHAR = 'char'
t_STRING = 'string'
t_BOOL = 'bool'
t_FLOAT = 'float'
t_LONG = 'long'
t_SHORT = 'short'
t_UNSIGNED = 'unsigned'
t_DOUBLE = 'double'
t_CLASS = 'class'
t_BREAK = 'break'
t_SWITCH = 'switch'
t_CASE = 'case'
t_IF = 'if'
t_ELSE = 'else'
t_RETURN = 'return'
t_TRUE = 'true'
t_FALSE = 'false'
t_INCLUDE = 'include'
t_USING = 'using'
t_NAMESPACE = 'namespace'
t_STD = 'std'
t_VOID = 'void'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUAL = r'\='
t_PLUS_PLUS = r'\++'
t_MINUS_MINUS = r'--'
t_EQUAL_EQUAL = r'=='
t_LEFT_BR = r'\('
t_RIGHT_BR = r'\)'
t_LEFT_BR_SQUARED = r'\['
t_RIGHT_BR_SQUARED = r'\]'
t_LEFT_BR_CURLY = r'\{'
t_RIGHT_BR_CURLY = r'\}'

t_NUMBER = r'(\d+(?:\.\d+)?)'
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'



