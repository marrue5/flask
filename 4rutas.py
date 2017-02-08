from flask import Flask
from flask import request   #Importamos request para poder pedir parametros en el url

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/params')
def params():
    param = request.args.get('params1', ' no contiene este parametro')   #Busca el de 'params1' en el url de la pagina. Si no esta guarda en la variable 'param' el segundo argumento de entrada. Para introducir un parametro en el url: http://127.0.0.1:8000/params?params1=mo
    return 'El parametro es{}'.format(param)                             #Pone en {} el valor de la variable param

#Con mas de un parametro

@app.route('/dosparams')
def dosparams():
    param1=request.args.get('param1', 'no contiene este parametro')
    param2=request.args.get('param2', 'no contiene este paremetro')
    return 'El parametro es:{}{}'.format(param1,param2)

#Para introducir un parametro en la url: http://127.0.0.1:8000/dosparams?param1=mo&param2=arrue
if __name__=='__main__':
    app.run(debug = True, port = 8000)