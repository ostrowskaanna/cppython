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
    'endl': 'ENDL',
    'cin': 'CIN',
    'cout': 'COUT'
}

tokens = [
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
             'OUT',
             'IN',
             'LESS',
             'LESS_EQUAL',
             'GREATER',
             'GREATER_EQUAL',
             'NOT_EQUAL',
             'AND',
             'OR',
             'HASH',
             'INT_NUMBER',
             'FLOAT_NUMBER',
             'VAR',
             'LIBRARY',
             'TEXT',
             'SIGN',
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
t_OUT = r'\<<'
t_IN = r'>>'
t_LESS = r'\<'
t_LESS_EQUAL = r'\<='
t_GREATER = r'\>'
t_GREATER_EQUAL = r'\>='
t_NOT_EQUAL = r'\!='
t_AND = r'\&&'
t_OR = r'\|\|'
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

t_LIBRARY = r'\<.*\>'

t_TEXT = r'\".*\"'

t_SIGN = r'\'.\''


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words if not in reserved words than its VAR
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


def p_start_symbol(p):
    '''
    start_symbol : program
    '''
    p[0] = p[1]


def p_program(p):
    '''
    program : program_components
            | empty
    '''
    p[0] = p[1]


def p_program_components(p):
    '''
    program_components : program_component
        | program_component program_components
        | empty
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


def p_program_component(p):
    '''
    program_component : function_definition
        | class_definition
        | including
        | var_declaration
        | array_declaration
        | empty
    '''
    p[0] = p[1]


# -----------------HEADERS------------------------------------------
'''
using_namespace_std : USING NAMESPACE STD SEMICOLON
'''

'''
including : HASH INCLUDE LIBRARY 
'''

# -----------------FUNCTION-------------------------------------------
'''
function_definition : type_function_definition 
    | void_function_definition 
'''

'''
type_function_definition : type VAR LEFT_BR function_var_declaration RIGHT_BR LEFT_BR_CURLY instructions returning RIGHT_BR_CURLY
'''

'''
void_function_definition : VOID VAR LEFT_BR function_var_declaration RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY
'''

'''
function_var_declaration : type VAR
    | empty
'''

# -----------------CLASS-------------------------------------------
'''
class_definition : CLASS STRING LEFT_BR_CURLY protection_level COLON class_declarations RIGHT_BR_CURLY SEMICOLON
'''

'''
protection_level " PUBLIC 
    | PRIVATE 
    | PROTECTED
'''

'''
class_declaration : var_declaration
    | function_definition
'''


def p_class_var_declarations(p):
    '''
    class_declarations : class_declaration
        | class_declaration class_declarations
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


# -----------------INSTRUCTIONS-------------------------------------------
def p_instructions(p):
    '''
    instructions : instruction
        | instruction instructions
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


'''
instruction : loop 
    | if_statement 
    | assignment 
    | operation 
'''

'''
while_loop : WHILE LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY 
'''

'''
for_loop_statement : FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER
    SEMICOLON increment RIGHT_BR
    | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS_EQUAL INT_NUMBER
    SEMICOLON increment RIGHT_BR
    | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR GREATER INT_NUMBER
    SEMICOLON decrement RIGHT_BR
    | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR GREATER_EQUAL INT_NUMBER
    SEMICOLON decrement RIGHT_BR
'''

'''
for_loop : for_loop_statement LEFT_BR_CURLY instructions RIGHT_BR_CURLY
'''

'''
loop : while_loop
    | for_loop
'''

'''
else_statement : ELSE LEFT_BR_CURLY instructions RIGHT_BR_CURLY
'''

'''
if_statement : IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY
'''


def p_comparisons(p):
    '''
    comparisons : comparison
        | comparison conjunction comparisons
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]


# -----------------EXPRESSIONS-------------------------------------------
'''
comparator : LESS
    | LESS_EQUAL
    | GREATER
    | GREATER_EQUAL
    | EQUAL_EQUAL
    | NOT_EQUAL
'''

'''
operator : PLUS
    | MINUS
    | MULTIPLY
    | DIVIDDE
'''

'''
type : INT
    | CHAR
    | STRING
    | BOOL
    | FLOAT
    | LONG
    | SHORT
'''

'''
conjunction : AND
    | OR
'''

'''
string_value : TEXT
    | SIGN
'''

'''
number : INT_NUMBER
    | FLOAT_NUMBER
'''

'''
bool_value : TRUE
    | FALSE
'''

'''
value : number
    | value
'''

'''
increment : VAR PLUS_PLUS SEMICOLON
'''

'''
decrement : VAR MINUS_MINUS SEMICOLON 
'''

'''
get_array_element : VAR LEFT_BR_SQUARED INT_NUMBER RIGHT_BR_SQUARED
'''

'''
operation : increment 
    | decrement 
    | value operator value SEMICOLON
'''

'''
assignment : VAR EQUAL value SEMICOLON
'''

'''
var_declaration : type VAR SEMICOLON
    | array_declaration 
'''

'''
array_declaration : type get_array_element SEMICOLON 
'''

'''
comparison : value comparator value 
'''

'''
returning : RETURN value SEMICOLON 
'''


def p_empty(p):
    '''empty : '''
    p[0] = ""


def p_error(p):
    print("parsing error\n")


parser = yacc.yacc()

while True:
    try:
        s = input("")
    except EOFError:
        break
    parser.parse(s)
