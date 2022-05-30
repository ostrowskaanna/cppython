import ply.yacc as yacc



def p_start_symbol(p):
    '''
    start_symbol : program
    '''
    p[0] = p[1]

def p_program(p):
    '''
    program : program_components
    '''
    p[0] = p[1]

def p_program_components(p):
    '''
    program_components : program_component
        | program_component program_components
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
    '''
    t[0] = t[1]

#-----------------HEADERS------------------------------------------
'''
using_namespace_std : USING NAMESPACE STD SEMICOLON
'''

'''
including : HASH INCLUDE LIBRARY 
'''

#-----------------FUNCTION-------------------------------------------
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

#-----------------CLASS-------------------------------------------
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

#-----------------INSTRUCTIONS-------------------------------------------
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
while_loop : WHILE LEFT_BR comparisions RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY 
'''

'''
for_loop_statemnt : FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER
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
if_statement : IF LEFT_BR comparisions RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY
'''


def p_comparisions(p):
    '''
    comparisions : comparision
        | comparision conjunction comparisions
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]


#-----------------EXPRESSIONS-------------------------------------------
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
comparision : value comparator value 
'''

'''
returning : RETURN value SEMICOLON 
'''

def p_empty(p):
    '''empty : '''
    p[0]=""

def p_error(p):
    print("parsing error\n")



parser = yacc.yacc()
data = ""
t = parser.parse(data)
print(t)
