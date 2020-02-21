from flask import Flask, request
import conmongo as mg

app = Flask(__name__)

@app.route('/hola')
def hello():
    pepe = {
        "nombre": "Luis",
        "edad": 30
    }
    return pepe


@app.route('/new/user',methods=['POST'])
def insertUser():
    nombre = request.form.getlist('name')
    mg.addUser(nombre)
    return "User insertado correctamente en la base de datos"


@app.route('/new/chat', methods=['POST'])
def insertChat():
    name = request.form.get('chat_name')
    participants = request.form.getlist('participants')
    mg.addChat(name,participants)
    return "Chat insertado correctamente en la base de datos"



















app.run("0.0.0.0", 5000, debug=True)
