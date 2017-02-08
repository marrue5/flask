from flask import Flask, render_template
import form11
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) #Añadimos los metodos GET y POST para poder trabajar con los datos que introduce el usuario en el formulario
def index():
    comment_form=form11.CommentForm(request.form)   #Busca un formulario en el fichero form11
    if request.method == 'POST':
        print(comment_form.username.data)       #Con esto estamos imprimiendo los tres campos introducidos por el usuario
        print(comment_form.email.data)
        print(comment_form.comment.data)

    title = "Curso Flask"
    return render_template('index5.html', title = title, form=comment_form)

if __name__=='__main__':
    app.run(debug = True, port = 8000)