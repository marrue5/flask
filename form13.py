#Aqui vamos a crear y definir todos nuestros formularios

from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class CommentForm(Form):        #La clase creada CommentForm se hereda de la clase importada FormCommentForm. Los atributos de la clase son los campos del formulario
    username = StringField('Username',
                           [validators.length(min=4, max=25, message='Ingrese un username válido')])       #Validacion para la longitud del username. message: mensaje que aparece si no cumple los requisitos.
    email = EmailField ('Correo electronico')
    comment = TextField ('Comentario')