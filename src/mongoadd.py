from pymongo import MongoClient
import src.checkfun as check
import src.sentimientos as sent
import random
from src.config import dbURL

client = MongoClient(dbURL)
db = client.get_database()
coll_user = db['users']
coll_chat = db['chats']
coll_message = db['messages']

#Funciones que añaden info a la base de datos
def addUser(nombre):
    """
    Checkea si existe un user en la bd y lo añade si no es así.
    """
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
    """
    Checkea si existe un chat y añade un chat nuevo con sus participantes.
    Necesita nombre y participantes como parámetros.
    """
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
    """
    Añade un mensaje a la bd. No se pueden duplicar mensajes.
    Necesita user,nombre de chat (válidos) y mensaje como parámetros
    en forma de diccionario.
    """
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