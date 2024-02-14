from lexico import *

precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

def p_expresion_declarar(t):
    'expresion : expresion MAS expresion'
    #   ^            ^      ^    ^
    #  t[0]         t[1]   t[2] t[3]
    t[0] = t[1] + t[3]