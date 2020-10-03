import tools.checkfun as check
import tools.sentimientos as sent
import random
from config.configuration import db, coll_user, coll_chat, coll_message


#Funciones que obtienen info de la base de datos
def chatUser(name):
    """
    Devuelve los grupos en los que está el usuario que le pidas.
    """
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
    """
    Devuelve todos los usuarios de la bd
    """
    users = list(coll_user.find({},{"_id":0, "name":1}))
    return users

def chats():
    """
    Devuelve todos los grupos/chats en la bd
    """
    grupos = list(coll_chat.find({},{"_id":0,"chat_name":1}))
    return grupos

def usersChat(name):
    """
    Devuelve todos los users que hay registrados en un chat
    en con creto que le pases como argumento.
    """
    if check.chat(name) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    
    query = {"chat_name": f"{name}"}
    users = list(coll_chat.find(query,{"_id":0}))
    return users


def messagesUser(user):
    """
    Devuelve todos los mensajes que ha escrito un usuario
    que le pases como argumento.
    """
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
    """
    Devuelve todos los mensajes que hay en la bd.
    """
    query = {}
    mensajes = list(coll_message.find(query,{"_id":0,"name_chat":0}))
    return mensajes


def messagesChat(name):
    """
    Devuelve todos los mensajes de un chat en concreto.
    """
    if check.chat(name) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    
    query = {"chat_name":f"{name}"}
    mensajes = list(coll_message.find(query,{"_id":0}))
    return mensajes


def sentimientosChat(name):
    """
    Llama a función que saca mensajes de un chat y lo pasa con formato
    para la función de analizar sentimientos.
    """
    if check.chat(name) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    
    mensajes = messagesChat(name)
    mens = [a.get('message')for a in mensajes]
    sentimientos_mensajes = sent.sentimientosMen(mens)
    return sentimientos_mensajes


def sentimientosUser(name,ran):
    """
    Llama a la función que extrae mensajes de un user
    y los formatea para pasarlos a la función que analiza sentimientos.
    """
    checkparam = "name"
    if check.user(checkparam,name) == True:
        pass
    else:
        error = "El usuario no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    mensajes = messagesUser(name)
    mens = [a.get('message')for a in mensajes]
    if ran == "N":
        sentimientos_mensajes = sent.sentimientosMen(mens)
    else:
        sentimientos_mensajes = sent.sentimientosMen(random.choice(mens))
    
    return sentimientos_mensajes

def sentimientosChatUser(name):
    """
    Encuentra los sentimientos de un determinado grupo y, además,
    extrae la polaridad de cada user en dicho grupo para devolver 
    ambas informaciones.
    """
    total = []
    mensajesgrupo = []
    if check.chat(name) == False:
        pass
    else:
        error = "El chat indicado no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    users = usersChat(name)
    listabien = users[0].get("participants")

    for a in listabien:
        query = {"$and":[{"chat_name":f"{name}"}, {"name":f"{a}"}]}
        mensajespers = list(coll_message.find(query,{"_id":0}))
        mensaje = [b.get("message") for b in mensajespers]
        polaridad = sent.sentimientosMen(mensaje)
        persona = {}
        persona[a] = polaridad
        mensajesgrupo.append(persona)
    
    sentotal = sentimientosChat(name)
    total.append(sentotal)
    total.append(mensajesgrupo)

    return total
