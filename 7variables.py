from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/')
@app.route('/user/<name>')
def index(name='Eduardo'):
    age = 19
    my_list = [1,2,3,4]
    return render_template('user.html',nombre=name, edad = age, list = my_list)        #Aplica el template user.html
                                                                                      #Les da valores a las variables que hay en el template user.html
if __name__=='__main__':
    app.run(debug = True, port = 8000)








