#Rutas que reciben parametros como una ruta (despues de /)

from flask import Flask
from flask import request   #Importamos request para poder pedir parametros en el url

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

#Devuelve el parametro introducido en el url
@app.route('/params/<name>/')
def params(name):
    return 'El parametro es: {}'.format(name)

#Devuelve el parametro introducido en el url y en caso que no se introduzca ningun parametro devuelve el parametro por defecto
@app.route('/params1/')
@app.route('/params1/<name>/')
def params1(name='Eso es un valor por defecto'):
    return 'El parametro es: {}'.format(name)

#Con dos parametros
@app.route('/params2/')
@app.route('/params2/<name>/')
@app.route('/params2/<name>/<last_name>')
def params2(name='Eso es un valor por defecto',last_name='Otro parametro por defecto'):
    return 'El parametro es: {}{}'.format(name,last_name)

if __name__=='__main__':
    app.run(debug = True, port = 8000)