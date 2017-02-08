from flask import Flask

app = Flask(__name__)   #Instancia de Flask, que recibe como parámetro __name__

@app.route('/')         #Decorador que indica la ruta a la que vamos a asociar nuestra funcion / lo que vamos a mostrar
def index():            #Función que se ejecuta cuando entramos a la pagina
    return 'Hola mundo'

app.run()               #Se encarga de ejecutar el servidor. Por default en el puerto 5000