import recomendaciones as rec   
from flask import Flask, request
import conmongo as mg
import json


app = Flask(__name__)

#Métodos POST para añadir info a la bd.

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

@app.route('/new/message',methods=['POST'])
def insertMessage():
    user = request.form.get('name')
    chat = request.form.get('chat_name')
    message = request.form.get('message')
    mg.addMessage(user,chat,message)
    return "Mensaje insertado correctamente en la base de datos"

#Métodos GET para obtener info de la API.

@app.route('/users')
def getUsers():
    info = mg.users()
    return json.dumps(info)


@app.route('/user/chat/<name>')
def getChatsUser(name):
    info = mg.chatUser(name)
    return json.dumps(info)

@app.route('/user/message/<name>')
def getMessageUser(name):
    info = mg.messagesUser(name)
    return json.dumps(info)

@app.route('/chat/message/<name>')
def getMessagesChat(name):
    info = mg.messagesChat(name)
    return json.dumps(info)

@app.route('/chat/sentiments/<name>')
def sentimentsChat(name):
    info = mg.sentimientosChat(name)
    return json.dumps(info)

@app.route('/user/sentiments/<name>')
def sentimentsUser(name):
    ran = "N"
    info = mg.sentimientosUser(name,ran)
    return json.dumps(info)


@app.route('/user/random/sentiments/<name>')
def sentimentsRandom(name):
    ran = "Y"
    info = mg.sentimientosUser(name,ran)
    return json.dumps(info)

@app.route('/recommend/<name>')
def recomendamosUser(name):
    info = rec.diccionarioGrande()
    return json.dumps(info)




app.run("0.0.0.0", 5000, debug=True)
