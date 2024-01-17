from ply import lex, yacc

# Lexer

tokens = ('NUMBER', 'PLUS', 'MINUS')

t_PLUS = r'\+'
t_MINUS = r'-'

t_ignore = ' \t\n'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at {p.value}")

parser = yacc.yacc()

# Test the compiler

def evaluate_expression(expression):
    result = parser.parse(expression)
    print(f"Result: {result}")

# Example usage
evaluate_expression("5 + 3 - 2")
evaluate_expression("10 - 4 + 2")
