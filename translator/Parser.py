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
             'COMMA',
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
t_COMMA = r'\,'
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

t_TEXT = r'"(.*?[^\\])"'

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


with open('TestInput\input2') as f:
    lines = f.readlines()

code = "".join(lines)

lexer = lex.lex()

lexer.input(code)

# -----------------------------------------------CREATING .PY FILE CONTENT----------------------------------------------
pythonCode = ""
elements = {}
num_of_tabs = 0
# -----------------------------------------------GRAMMAR----------------------------------------------------------------

def p_start_symbol(p):
    '''
    start_symbol : program
    '''
    p[0] = p[1]
    print(p[0])


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
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = p[1] + p[2]


def p_program_component(p):
    '''
    program_component : function_definition
        | class_definition
        | including
        | using_namespace_std
        | var_declaration
        | array_declaration
        | comment
        | empty
    '''
    p[0] = p[1]

# -----------------HEADERS------------------------------------------
def p_using_namespace_std(p):
    '''
    using_namespace_std : USING NAMESPACE STD SEMICOLON
    '''
    p[0] = ""
    #print(p[0])
    elements["using_namespace_std"] = p[0]

def p_including(p):
    '''
    including : HASH INCLUDE LIBRARY
    '''
    p[0] = ""
    #print(p[0])
    elements["including"] = p[0]

# -----------------FUNCTION-------------------------------------------
def p_function_definition(p):
    '''
    function_definition : type_function_definition
        | void_function_definition
    '''
    p[0] = p[1]


def p_type_function_definition(p):
    '''
    type_function_definition : type VAR LEFT_BR function_var_declaration RIGHT_BR LEFT_BR_CURLY change_tab_number instructions returning RIGHT_BR_CURLY
    '''
    p[0] = "def " + p[2] + p[3] + str(p[4]) + p[5] + ":\n" + str(p[8]) + "\n"
    global num_of_tabs
    num_of_tabs -= 1


# 0 - None, 1 - 'void', 2 - Name, 3 - '(', 4 - None (arguments list), 5 - ')', 6 - '{', 7 - None (instructions), 8 - '}'
def p_void_function_definition(p):
    '''
    void_function_definition : VOID VAR LEFT_BR function_var_declaration RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
    '''
    p[0] = "def " + p[2] + p[3] + str(p[4]) + p[5] + ":\n" + str(p[8]) + "\n"
    global num_of_tabs
    num_of_tabs -= 1
    #print("function type: ", p[1])
    #print("function name: ", p[2])


def p_function_var_declaration(p):
    '''
    function_var_declaration : var_declaration_no_semicolon
        | var_declaration_no_semicolon COMMA function_var_declaration
        | empty
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
         p[0] = p[1] + p[2] + p[3]

def p_var_declaration_no_semicolon(p):
    '''
    var_declaration_no_semicolon : type VAR
    '''
    p[0] = p[1] + p[2]
    #print("var passed to function: ", p[0])

# -----------------CLASS-------------------------------------------
def p_class_definition(p):
    '''
    class_definition : CLASS VAR LEFT_BR_CURLY protection_level class_declarations RIGHT_BR_CURLY SEMICOLON
    '''


def p_protection_level(p):
    '''
    protection_level : PUBLIC COLON
        | PRIVATE COLON
        | PROTECTED COLON
        | empty
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = p[1] + p[2]


def p_class_declaration(p):
    '''
    class_declaration : var_declaration
        | function_definition
    '''
    p[0] = p[1]

def p_class_declarations(p):
    '''
    class_declarations : class_declaration
        | class_declaration class_declarations
        | empty
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = p[1] + p[2]

# -----------------INSTRUCTIONS-------------------------------------------
def p_instructions(p):
    '''
    instructions : instruction
        | instruction instructions
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = p[1] + p[2]

def p_instruction(p):
    '''
    instruction : loop
        | if_statement
        | assignment
        | operation
        | empty
        | var_declaration
        | print
        | input
        | comment
    '''
    global num_of_tabs
    tabs = ""
    for i in range(num_of_tabs):
        tabs += "    "
    p[0] = tabs + p[1]

def p_while_loop(p):
    '''
    while_loop : WHILE LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
        | WHILE LEFT_BR bool_value RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
    '''
    p[0] = p[1] + " " + p[3] + ":\n" + p[7] + "\n"
    global num_of_tabs
    num_of_tabs -= 1
    #print("while loop: ", p[0])

def p_for_loop_statement(p):
    '''
    for_loop_statement : FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER SEMICOLON VAR PLUS_PLUS RIGHT_BR
        | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS_EQUAL INT_NUMBER SEMICOLON VAR PLUS_PLUS RIGHT_BR
        | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR GREATER INT_NUMBER SEMICOLON VAR MINUS_MINUS RIGHT_BR
        | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR GREATER_EQUAL INT_NUMBER SEMICOLON VAR MINUS_MINUS RIGHT_BR
    '''
    start_range = None
    end_range = None
    decrement = False
    if p[9] == '<':
        start_range = p[6]
        end_range = p[10]
    if p[9] == '<=':
        start_range = p[6]
        end_range = str(int(p[10]) + 1)
    if p[9] == '>':
        start_range = p[6]
        end_range = p[10]
        decrement = True
    if p[9] == '>=':
        start_range = p[6]
        end_range = str(int(p[10]) - 1)
        decrement = True
    if decrement:
        p[0] = p[1] + " " + p[4] + " in range(" + str(start_range) + ", " + str(end_range) + ", -1)"
    else:
        p[0] = p[1] + " " + p[4] + " in range(" + str(start_range) + ", " + str(end_range) + ")"


def p_for_loop(p):
    '''
    for_loop : for_loop_statement LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
    '''
    p[0] = p[1] + ":\n" + p[4] + "\n"
    global num_of_tabs
    num_of_tabs -= 1
    #print("for loop: ", p[0])


def p_loop(p):
    '''
    loop : while_loop
        | for_loop
    '''
    p[0] = p[1]


def p_else_statement(p):
    '''
    else_statement : ELSE LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
    '''
    p[0] = p[1] + ":\n" + p[4] + "\n"
    global num_of_tabs
    num_of_tabs -= 1


def p_if_statement(p):
    '''
    if_statement : IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
                 | IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY else_statement
    '''
    if(len(p) == 9):
        p[0] = p[1] + " " + p[3] + ":\n" + str(p[7]) + "\n"
    elif(len(p) == 10):
        p[0] = p[1] + " " + p[3] + ":\n" + str(p[7]) + "\n" + p[9]


def p_comparisons(p):
    '''
    comparisons : comparison
        | comparison conjunction comparisons
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]


def p_comparison(p):
    '''
    comparison : value comparator value
    '''
    p[0] = str(p[1]) + " " + p[2] + " " + str(p[3])

# -----------------EXPRESSIONS-------------------------------------------
def p_comparator(p):
    '''
    comparator : LESS
        | LESS_EQUAL
        | GREATER
        | GREATER_EQUAL
        | EQUAL_EQUAL
        | NOT_EQUAL
    '''
    p[0] = p[1]


def p_operator(p):
    '''
    operator : PLUS
        | MINUS
        | MULTIPLY
        | DIVIDE
    '''
    p[0] = p[1]


def p_type(p):
    '''
    type : INT
        | CHAR
        | STRING
        | BOOL
        | FLOAT
        | LONG
        | SHORT
        | DOUBLE
    '''
    p[0] = ""


def p_conjunction(p):
    '''
    conjunction : AND
        | OR
    '''
    p[0] = p[1]


def p_string_value(p):
    '''
    string_value : TEXT
        | SIGN
    '''
    p[0] = p[1]


def p_number(p):
    '''
    number : INT_NUMBER
        | FLOAT_NUMBER
    '''
    p[0] = p[1]


def p_bool_value(p):
    '''
    bool_value : TRUE
        | FALSE
    '''
    p[0] = p[1]


def p_value(p):
    '''
    value : number
        | VAR
        | get_array_element
        | string_value
        | bool_value
    '''
    p[0] = p[1]


def p_increment(p):
    '''
    increment : VAR PLUS_PLUS SEMICOLON
    '''
    p[0] = p[1] + " += 1\n"
    #("incrementation: ", p[0])


def p_decrement(p):
    '''
    decrement : VAR MINUS_MINUS SEMICOLON
    '''
    p[0] = p[1] + " -= 1\n"
    #("decrementation: ", p[0])


def p_get_array_element(p):
    '''
    get_array_element : VAR LEFT_BR_SQUARED INT_NUMBER RIGHT_BR_SQUARED
    '''
    p[0] = p[1] + p[2] + str(p[3]) + p[4]


def p_operation(p):
    '''
    operation : increment
        | decrement
        | value operator value SEMICOLON
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 5):
        p[0] = p[1] + p[2] + p[3] + "\n"


def p_assignment(p):
    '''
    assignment : VAR EQUAL value SEMICOLON
               | VAR EQUAL VAR SEMICOLON
               | get_array_element EQUAL value SEMICOLON
               | get_array_element EQUAL VAR SEMICOLON
    '''
    p[0] = p[1] + " " + p[2] + " " + str(p[3]) + "\n"
    #("assignment: ", p[0])

def p_var_declaration(p):
    '''
    var_declaration : type VAR SEMICOLON
        | array_declaration
        | type VAR EQUAL value SEMICOLON
        | type VAR EQUAL VAR SEMICOLON
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = p[1] + p[2] + " = None\n"
    elif(len(p) == 6):
        p[0] = p[1] + " " + p[2] + p[3] + str(p[4] + p[5])


def p_array_declaration(p):
    '''
    array_declaration : type get_array_element SEMICOLON
    '''
    name = p[2].split('[')[0]
    p[0] = name + " = []\n"
    #("array declaration: ", p[0])


def p_out(p):
    '''
    out : OUT VAR
        | OUT VAR out
        | OUT TEXT
        | OUT TEXT out
        | OUT ENDL
        | OUT ENDL out
    '''
    if(len(p) == 3):
        if p[2] == 'endl':
            p[0] = '"\\n"'
        else:
            p[0] = p[2]
    elif(len(p) == 4):
        if p[2] == 'endl':
            p[0] = '"\\n"' + "," + p[3]
        else:
            p[0] = p[2] + "," + p[3]


def p_in(p):
    '''
    in : IN VAR
       | IN VAR in
    '''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    elif(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]


def p_print(p):
    '''
    print : COUT out SEMICOLON
    '''
    p[0] = "print(" + str(p[2]) + ")\n"
    #print("printing: ", p[0])


def p_input(p):
    '''
    input : CIN in SEMICOLON
    '''
    p[0] = p[1] + p[2] + p[3]


def p_returning(p):
    '''
    returning : RETURN value SEMICOLON
    '''
    p[0] = p[1] + " " + p[2] + "\n"

def p_comment(p):
    '''
    comment : COMMENT
    '''
    p[0] = p[1]

def p_empty(p):
    '''empty : '''
    p[0] = ""


def p_error(p):
    print("Syntax error at '%s'\n" % p.value)


# -------------------------------------FUNCTIONS TO HANDLE ACTIONS------------------------------------------------------
def p_change_tab_number(p):
    "change_tab_number : "
    global num_of_tabs
    num_of_tabs += 1


parser = yacc.yacc()
parser.parse(code)



lexer = lex.lex()

lexer.input(code)

'''
while True:
    tok = lexer.token()
    if not tok:
        break
    else:
        print(tok)
'''