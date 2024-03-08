import ply.yacc as yacc
from lexico import tokens

listaSentencias = []
#Derivacion Inicial
precedence = ( #ORGANIZAMOS DE LA JERARQUIA DE OP. LOGICOS
   ('right','ASING'),
   ('right','IGUAL'),
   ('left','MAYOR','MENOR'),
   ('left','MAS','MENOS'),
   ('left','MULT','DIV'),
   ('left','IPAREN','RPAREN'),
   ('left','ILLAVE','RLLAVE')
   )

def p_program(p):
    'program : sent'
    p[0] = p[1]
    print("Derivacion Inicial")
# def p_sent(p):
#     '''sent : if_instr
#             | for_instr
#             | while_instr
#             | print
#             | dec_val
#             | sing_val
#             | dec_array'''
#     global listaSentencias
#     listaSentencias.append("Instruccion")
#     p[0] = p[1]

def p_sent_if(p):
    'sent : if_instr'
    global listaSentencias
    listaSentencias.append(1)
    print("Derivacion Sentencia if")
    p[0] = p[1]
    
def p_sent_for(p):
    'sent : for_instr'
    global listaSentencias
    listaSentencias.append(2)
    print("Derivacion Sentencia for")
    p[0] = p[1]
    
def p_sent_while(p):
    'sent : while_instr'
    global listaSentencias
    listaSentencias.append(3)
    print("Derivacion Sentencia while")
    p[0] = p[1]
    
def p_sent_print(p):
    'sent : print'
    global listaSentencias
    print("Derivacion Sentencia print")
    listaSentencias.append(4)
    p[0] = p[1]
    
def p_sent_dec_val(p):
    'sent : dec_val'
    global listaSentencias
    listaSentencias.append(5)
    print("Derivacion declaracion de variable")
    p[0] = p[1]
    
def p_sent_sing_val(p):
    'sent : sing_val'
    global listaSentencias
    listaSentencias.append(6)
    print("Derivacion asignacion de valor")
    p[0] = p[1]
    
def p_sent_dec_array(p):
    'sent : dec_array'
    global listaSentencias
    listaSentencias.append(7)
    print("Derivacion declaracion de arreglo")
    p[0] = p[1]
    
def p_sent_empty(p):
    'sent : empty'
    
#Instruccion IF        
def p_if_instr(p):
    'if_instr : IF IPAREN exp_logic RPAREN ILLAVE sent RLLAVE'
    print("Derivacion estructura if")
    if(p[3]):
        p[0] = p[6]
#Instruccion IF-ELSE
def p_if_else_instr(p):
    'if_instr : IF IPAREN exp_logic RPAREN ILLAVE sent RLLAVE ELSE ILLAVE sent RLLAVE'
    print("Derivacion estructura if-else")
    p[0] = [p[3]] + [p[9]]
#Intruccion FOR
def p_for_instr(p):
    'for_instr : FOR IPAREN sing_val exp_logic PUNTOCOMA op_idec RPAREN ILLAVE sent RLLAVE'
    print("Derivacion estructura for")
    p[0] = [p[3]] + [p[5]] + [p[7]] + [p[10]]
#Instruccion WHILE
def p_while_instr(p):
    'while_instr : WHILE IPAREN exp_logic RPAREN ILLAVE sent RLLAVE'
    print("Derivacion estructura while")
    p[0] = [p[3]] + [p[6]]
#Instruccion PRINT
def p_print_instr(p):
    'print : SYSTEM PUNTO OUT PUNTO PRINTL IPAREN valor_cadena RPAREN PUNTOCOMA'
    print("Derivacion estructura print")
    p[0] = p[7]
#Declaracion de variable
def p_dec_val(p):
    'dec_val : tipo ID rest_dec PUNTOCOMA'
    print("Derivacion estructura declaracion de variable")
    p[0] = [p[1]] + [p[3]]
#Resto de la declaracion
def p_rest_dec_val(p):
    'rest_dec : COMA ID rest_dec'
    print("Derivacion estructura resto de la declaracion")
    p[0] = [p[1]] + [p[3]]
#Resto declaracion vacia
def p_rest_dec_final(p):
    'rest_dec : '
    print("Derivacion estructura resto vacio")
    #No Hace Nada Por que no quiero
#Asignacion de valor
def p_sing_val(p):
    'sing_val : ID ASING term PUNTOCOMA '
#Asignacion de expresion
def p_sing_exp_arit(p):
    'sing_val : ID ASING exp_arit PUNTOCOMA '
#Declaracion de array
def p_dec_array(p):
    'dec_array : ICORCH RCORCH ID PUNTOCOMA'
#Tipos de datos
def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR
            | DOUBLE
            | BOOLEAN
            | STRING'''
    p[0] = p[1]
    print("Derivacion asigancion de tipo")
#########################Expresion Logica###########################
def p_exp_logic(p):
    'exp_logic : exp_rel'
    print("Derivacion exprecion logica")
    p[0] = p[1]
#Termino Logico
def p_exp_term(p):
    'exp_logic : term_bool'
    print("Expresion a termino booleano")
    p[0] = p[1]
#Expresion Logica And
def p_exp_logic_and(p):
    'exp_logic : exp_logic AND exp_logic'
    print("Derivacion exprecion logico estructura con AND")
    p[0] = p[1] + p[3]
#Expresion Logica OR
def p_exp_logic_or(p):
    'exp_logic : exp_logic OR exp_logic'
    print("Derivacion exprecion logico estructura con AND")
    p[0] = p[1] + p[3]
#Expresion Logica NOT
def p_exp_logic_not(p):
    'exp_logic : NOT exp_logic'
    p[0] = p[2]
#Expresiones Relacionales 
def p_exp_rel(p):
    'exp_rel : exp_arit op_rel exp_arit'
    p[0] = p[1] 
#Exprecion telacional con terminos
def p_exp_rel_term(p):
    'exp_rel : exp_rel op_rel term'
    p[0] = p[1] 
#Expresiones Aritmeticas MAS
def p_exp_arit_mas(p):
    'exp_arit : exp_arit MAS term_arit'
    p[0] = p[1] + p[3]
#Expresiones Aritmeticas MENOS
def p_exp_arit_menos(p):
    'exp_arit : exp_arit MENOS term_arit'
    p[0] = p[1] - p[3]
#Expresiones Aritmeticas - Termino Aritmetico
def p_exp_term_arit(p):
    'exp_arit : term_arit'
    p[0] = p[1]
#Termino Aritmetico Multiplicacion
def p_term_arit_mult(p):
    'term_arit : term_arit MULT fact_arit'
    p[0] = p[1] * p[3]
#Termino Aritmetico Divicion
def p_term_arit_div(p):
    'term_arit : term_arit DIV fact_arit'
    p[0] = p[1] / p[3]

def p_term_fact(p):
    'term_arit : fact_arit'
    p[0] = p[1] 
#Factor Aritmetico en Parentecis
def p_fact_arit_paten(p):
    'fact_arit : IPAREN exp_arit RPAREN'
    p[0] = p[2]
#Factor Aritmetico ID
def p_fact_arit_id(p):
    'fact_arit : ID'
    p[0] = p[1]
#Fator Aritmetico ENTERO
def p_fact_arit_entero(p):
    'fact_arit : ENTERO'
    p[0] = p[1]
#Factor Aritmetico DECIMAL
def p_fact_arit(p):
    'fact_arit : DECIMAL'
    p[0] = p[1]
#Valor Cadena
def p_cadena(p):
    'valor_cadena : CADENA'
    print("Signacion Valor Cadena ")
    p[0] = p[1]
    
def p_cadena_id(p):
    'valor_cadena : CADENA MAS ID'
    print("Signacion Valor Cadena ")
    p[0] = p[1]
    
def p_cadena_numero(p):
    'valor_cadena : CADENA MAS ENTERO'
    print("Signacion Valor Cadena ")
    p[0] = p[1]

#Operadores Relaciones 
def p_op_rel(p):
    '''op_rel : IGUAL
              | MAYOR
              | MENOR
              | DIF
              | MAYORIGUAL
              | MENORIGUAL'''
    p[0] = p[1] 
#Terminos
def p_term(p):
    '''term : fact_arit
            | term_bool'''
    p[0] = p[1]
#Termino Boleano
def p_term_bool_true(p):
    '''term_bool : TRUE 
                 | FALSE'''
    print("Signacion valor boolean")
    p[0] = p[1]

def p_op_inc_dec(p):
    '''op_idec : ID INC
                | ID DEC
                | DEC ID
                | INC ID'''
    p[0] = p[1]
    
def p_empty(p):
    'empty : '
    pass
#######################Expresion Logica########################33
error = ""
# Error rule for syntax errors
bandera = ""
def p_error(p):   
    global error
    global bandera
    print("Entre")
    error = "" 
    if p:
        error = p
        print("sintactico.py IF -> Error en token ", p)
    else:
        error = "EOF"
        print("sintactico.py IF -> Error: se encontró EOF")
    bandera="No"
    return bandera

# Build the parser
def analizarEstructura(dato):
    global bandera
    bandera = "Si"
    parser = yacc.yacc()
    print("No Entro")
    result = parser.parse(dato)
    return bandera