import ply.lex as lex

linea = 1
valor = " "
resultadoLexema =[]
#Palabras Reservadas
res = (
    'FOR','WHILE','IF',
    'ELSE','TRUE','FALSE',
    'SYSTEM','OUT','PRINTL')
#Tipo Variable
tipo = (
    'INT','FLOAT',
    'CHAR','DOUBLE',
    'BOOLEAN','STRING')
#Opetadores Logicos
opA = ('MAS','MENOS',
        'MULT','DIV',
        'ASING')
#Operadores De Incremento y Decremento
opID = ('INC','DEC')
#Operadores Logicos
opL = ('NOT','AND','OR')
#Operadores Relacionales
opR = ('IGUAL','MAYOR','MENOR',
       'DIF','MAYORIGUAL',
       'MENORIGUAL')
#Delimitadores 
deli = ('IPAREN','RPAREN',
        'ICORCH','RCORCH',
        'ILLAVE','RLLAVE',)
#Tokens
tokens = ('ID','ENTERO','PUNTO',
          'DECIMAL','CADENA',
          'PUNTOCOMA','COMA') 

tokens = tokens + res + tipo + opA + opID + opL + opR + deli

#OPERADORES ARITMETICOS
t_MAS =r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_ASING = r'\='
#OPERADORES DE INCREMENTO Y DECREMENTO 
t_INC = r'\+\+'
t_DEC = r'--'
#OPERADORES RELACIONALES
t_IGUAL = r'=='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DIF = r'!='
#OPERADORES LOGICOS
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'   
#OPERADOR DE ACCESO
t_PUNTO = r'\.'
t_COMA = r','
t_PUNTOCOMA = r';'
#DELIMITADORES
t_IPAREN = r'\('
t_RPAREN = r'\)'
t_ICORCH = r'\['
t_RCORCH = r'\]'
t_ILLAVE = r'\{'
t_RLLAVE = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'    
    if (t.value.upper() in res) or (t.value.upper() in tipo):
        t.type = t.value.upper()
    else:
        t.type = str("ID")
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try: 
        t.value = float(t.value)
    except ValueError:
        t.type = str("INVALIDO")
    return t

def t_ENTERO(t):
    r'\d+'
    try: 
        t.value = int(t.value)
    except ValueError:
        t.type = str("INVALIDO")
    return t

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] #removemos comillas
    #Agregar todas las acciones como tap,saltos y mas
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    t.type = str("CADENA")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
        estado = {
            "identificador": "DESCONOCIDO",
            "lexema": str(t.value),
            "linea": str(linea)
        }
        cadena = str(t.value)
        valor = len(cadena)
        t.lexer.skip(valor)
        resultadoLexema.append(estado)

def test(data):
    global linea
    global resultadoLexema
    lexer = lex.lex()
    datosAux =  data.split("\n")
    for aux1 in datosAux:
        aux2 =  aux1.split(" ")
        for dato in aux2:
            lexer.input(dato)
            while True:
                tok = lexer.token()
                if not tok:
                    break
                estado = {
                    "token": str(tok.value),
                    "lex": str(tok.type),
                    "linea": str(linea)
                }
                resultadoLexema.append(estado)
                print("Limea",resultadoLexema)
                valor=" "
        linea += 1
