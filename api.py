import src.recomendaciones as rec   
from flask import Flask, request
import src.conmongo as mg
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
#get usuario
@app.route('/users')
def getUsers():
    info = mg.users()
    return json.dumps(info)

#get chats en los que está un user
@app.route('/user/chat/<name>')
def getChatsUser(name):
    info = mg.chatUser(name)
    return json.dumps(info)

#get todos los grupos creados
@app.route('/chats')
def getChats(): 
    info = mg.chats()
    return json.dumps(info)

#get todos los mensajes de un user
@app.route('/user/message/<name>')
def getMessageUser(name):
    info = mg.messagesUser(name)
    return json.dumps(info)

#get todos los mensajes de un chat
@app.route('/chat/message/<name>')
def getMessagesChat(name):
    info = mg.messagesChat(name)
    return json.dumps(info)

# Get sentimientos de un chat
@app.route('/chat/sentiments/<name>')
def sentimentsChat(name):
    info = mg.sentimientosChat(name)
    return json.dumps(info)
#get sentimientos de un usuario
@app.route('/user/sentiments/<name>')
def sentimentsUser(name):
    ran = "N"
    info = mg.sentimientosUser(name,ran)
    return json.dumps(info)
#get sentimientos de un mensaje random de un usuario
@app.route('/user/random/sentiments/<name>')
def sentimentsRandom(name):
    ran = "Y"
    info = mg.sentimientosUser(name,ran)
    return json.dumps(info)

# Get recomendaciones
@app.route('/recommend/<name>')
def recomendamosUser(name):
    info = rec.recomiendaUser(name)
    return json.dumps(info)




app.run("0.0.0.0", 5000, debug=True)
