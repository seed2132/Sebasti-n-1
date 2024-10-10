from flask import Flask
from flask_cors import CORS
import numpy as np
app = Flask(__name__)
CORS(app)

@app.route('/')
def hola_mundo():
    return '<h1>Hola Mundo!</h1>'

@app.route('/ruta2')
def ruta2():
    return '<h1>Estás en la ruta 2</h1>'

@app.route('/ruta3')
def ruta3():
    return '<h1>Estás en la ruta 3</h1>'

@app.route('/ecuacion')
@app.route('/ecuacion/<float:x>/<float:z>')
def ecuacion(x=0,z=0):
    y = x* z + z+ x
    return f"<h1>El resultado de la ecuación es {y}</h1>"

@app.route('/multiplicar')
@app.route('/multiplicar/<int:valor1>')
def multiplicacion(valor1=0):
    tabla = np.arange(1,11) * valor1
    return f"<h1>La tabla de {valor1} es {tabla}</h1>"

@app.route('/calcular')
@app.route('/calcular/circulo/<float:radio>/')
def calcular_circulo(radio=0):
    area = np.pi * np.power(radio,2)
    return f"<h1>El área del círculo es {area}</h1>"

@app.route('/calcular/cuadrado/<float:lado>')
def calcular_cuadrado(lado=0):
    area = lado * lado
    return f"<h1>El área del cuadrado es {area}</h1>"

@app.route('/calcular/triangulo/<float:base>/<float:altura>')
def calcular_triangulo(base=0,altura=0):
    area= (base*altura)/2
    return f"<h1>El área del triángulo es {area}</h1>"

    
if __name__ == '__main__':
   app.run(debug=True)