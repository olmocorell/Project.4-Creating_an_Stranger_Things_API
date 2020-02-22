from pymongo import MongoClient
import checkfun as check
from bson.json_util import dumps
import json
import sentimientos as sent
import random

client = MongoClient("mongodb://localhost:27017/apidb")
db = client.get_database()
coll_user = db['users']
coll_chat = db['chats']
coll_message = db['messages']

#Funciones que añaden info a la base de datos
def addUser(nombre):
    checkparam = "name"
    if check.user(nombre,checkparam) == True:
        pass
    else:
        error = 'Ya existe un usuario con ese user_id en la base de datos'
        raise ValueError (error)
    query = {}
    identity=list(coll_user.find(query,{"_id":0,"name":1}))

    dict_insert={
        'user_id': f'{len(identity)}',
        'name':nombre
    }
    coll_user.insert_one(dict_insert)
    

def addChat(name,participants):
    if check.chat(name) == True:
        pass
    else:
        error = 'Ya existe un chat con ese nombre en la base de datos'
        raise ValueError (error)

    for a in participants:
        if check.user(a,name) == True:
            pass
        else:
            error = f"No existe el usuario {a}"
            raise ValueError(error)
    
    dict_insert = {
        'chat_name': f'{name}',
        'participants': participants
    }
    coll_chat.insert_one(dict_insert)


def addMessage(user,chat,message):   
    checkparam = "name" 
    if check.chat(chat) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    if check.user(checkparam,user) == True:
        pass
    else:
        error = "El usuario no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)

    if check.userInChat(chat,user) == True:
        pass
    else:
        error = "Ese usuario no pertenece a ese chat"
        raise ValueError(error)

    if check.message(message) == False:
        pass
    else:
        error = "Ese mensaje ya existe en la base de datos"
        raise ValueError(error)

    dict_insert = {
        'name': f'{user}',
        'chat_name': f'{chat}',
        'message': f'{message}'
    }
    coll_message.insert_one(dict_insert)

#Funciones que obtienen info de la base de datos

def chatUser(name):
    checkparam = "name" 
    if check.user(checkparam,name) == True:
        pass
    else:
        error = "El usuario no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)

    query = {"participants": f"{name}"}
    grupos = list(coll_chat.find(query,{"_id":0,"chat_name":1}))
    return grupos

def users():
    users = list(coll_user.find({},{"_id":0, "name":1}))
    return users

def messagesUser(user):
    checkparam = "name" 
    if check.user(checkparam,user) == True:
        pass
    else:
        error = "El usuario no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)

    query = {"name":f"{user}"}
    mensajes = list(coll_message.find(query,{"_id":0}))
    return mensajes

def todosLosMensajes():
    query = {}
    mensajes = list(coll_message.find(query,{"_id":0,"name_chat":0}))
    return mensajes



def messagesChat(name):
    if check.chat(name) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    
    query = {"chat_name":f"{name}"}
    mensajes = list(coll_message.find(query,{"_id":0}))
    return mensajes


def sentimientosChat(name):
    if check.chat(name) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)

    query = {"chat_name":f"{name}"}
    mensajes = list(coll_message.find(query,{"_id":0}))
    mens = [a.get('message')for a in mensajes]
    sentimientos_mensajes = sent.sentimientosMen(mens)
    return sentimientos_mensajes

def sentimientosUser(name,ran):

    checkparam = "name"
    if check.user(checkparam,name) == True:
        pass
    else:
        error = "El usuario no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)

    query = {"name":f"{name}"}
    mensajes= list(coll_message.find(query,{"_id":0}))
    mens = [a.get('message')for a in mensajes]
    if ran == "N":
        sentimientos_mensajes = sent.sentimientosMen(mens)
    else:
        sentimientos_mensajes = sent.sentimientosMen(random.choice(mens))
    
    return sentimientos_mensajes

