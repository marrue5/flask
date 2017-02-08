from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

if __name__=='__main__':
    app.run(debug = True, port = 8000)        #Cantidad de puertos que tiene nuestro ordenador: 2^16, pero los primeros 1024 estan ocupados. En este caso utilizamos el 8000
                                              #Si ponemos debug = true, no hace falta que ejecutemos el programa cada vez que cambiamos algo, sino que lo hace automaticamente. Los cambios se ven reflejados directamente.