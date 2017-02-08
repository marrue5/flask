from flask import Flask
from flask import render_template


# Si nuestra carpeta de templates no se llama templates, poner app = Flask(__name__, template_folder = "nombre_carpeta")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

if __name__=='__main__':
    app.run(debug = True, port = 8000)