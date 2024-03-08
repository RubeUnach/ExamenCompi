from flask import Flask, render_template, request
from lexico import * 
from sintaxis import *
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/lex', methods=['POST'])
def lexema():
    data = request.get_json()
    codigo = data.get('data')
    test(codigo)
    bandera = analizarEstructura(codigo)
    print("Valor ==",bandera)
    return render_template('analicis.html',tokens = resultadoLexema, condicion = bandera)
    
if __name__ == '__main__':
    app.run()