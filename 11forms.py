from flask import Flask, render_template
import form11

app = Flask(__name__)

@app.route('/')
def index():
    comment_form=form11.CommentForm()
    title = "Curso Flask"
    return render_template('index5.html', title = title, form=comment_form)

if __name__=='__main__':
    app.run(debug = True, port = 8000)