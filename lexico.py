import ply.lex as lex

class Lexico():
    
    linea = 1
    rlexema = []
    valor = "IDENTIFICADOR"
    
    reservados = (
        'FOR','DO','WHILE',
        'IF','ELSE','SWITCH',
        'CASE','BREAK','RETURN',
        'STATIC','PRINT','INT',
        'FLOAT','VOID','CHAR',
        'PUBLIC','PRIVATE',
    )
    operadores = ('MAS','MENOS','MULT','DIV','ASIG')
    delimitadores = ('IPAREN','RPAREN','ICORCH','RCORCH','ILLAVE','RLLAVE',)
    tokens = ('IDENTIFICADOR','ENTERO','DECIMAL','CADENA','FIN',) + reservados + operadores + delimitadores
    #OPERADORES
    t_MAS =r'\+'
    t_MENOS=r'-'
    t_MULT=r'\*'
    t_DIV=r'/'
    t_ASIG=r'='
    #DELIMITADORES
    t_IPAREN=r'\('
    t_RPAREN=r'\)'
    t_ICORCH=r'\['
    t_RCORCH=r'\]'
    t_ILLAVE=r'\{'
    t_RLLAVE=r'\}'
        
    def t_FIN(self,t):
        r';'
        self.valor = "FIN"
        return t

    def t_IDENTIFICADOR(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if t.value.upper() in self.reservados:
            self.valor = "RESERVADA"
        else:
            self.valor = "IDENTIFICADOR"
        return t
    
    def t_DECIMAL(self,t):
        r'\d+\.\d+'
        try: 
            t.value = float(t.value)
            self.valor = "NUMERO"
        except ValueError:
            self.valor = "INVALIDO"
        return t

    def t_ENTERO(self,t):
        r'\d+'
        try: 
            t.value = int(t.value)
            self.valor = "NUMERO"
        except ValueError:
            self.valor = "INVALIDO"
        return t

    def t_CADENA(self,t):
        r'(\".*?\")'
        t.value = t.value[1:-1] #removemos comillas
        #Agregar todas las acciones como tap,saltos y mas
        t.value = t.value.replace('\\t','\t')
        t.value = t.value.replace('\\n','\n')
        t.value = t.value.replace('\\"','\"')
        t.value = t.value.replace("\\'","\'")
        t.value = t.value.replace('\\\\','\\')
        self.valor = "CADENA"
        return t
    
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore  = ' \t'

    def t_error(self,t):
        estado = {
            "token": "INVALIDO",
            "lexema": str(t.value),
            "linea": str(self.linea)
        }
        cadena = str(t.value)
        valor = len(cadena)
        t.lexer.skip(valor)
        self.rlexema.append(estado)

    def test(self,data):
        self.lexer = lex.lex(self)
        datosAux =  data.split("\n")
        for aux1 in datosAux:
            aux2 =  aux1.split(" ")
            for dato in aux2:
                self.lexer.input(dato)
                while True:
                    tok = self.lexer.token()
                    if not tok:
                        break
                    if str(tok.type) in self.operadores:
                        self.valor = "OPERADOR"
                    elif str(tok.type) in self.delimitadores:
                        self.valor = "SIMBOLO"
                    estado = {
                        "token": self.valor,
                        "lexema": str(tok.value),
                        "linea": str(self.linea)
                    }
                    self.rlexema.append(estado)
            self.linea += 1
        return self.rlexema
    
    def borrar(self):
        self.rlexema.clear()