from pymongo import MongoClient
from config.configuration import db, coll_user, coll_chat, coll_message



def user(name,search):
    """
    Checkeamos que el usuario exista en la base de datos.
    Es una función reutilizable para todos los checks.
    Devuelve TRUE si el usuario NO EXISTE
    Hay que indicarle a la función si buscamos por id_user o por name.
    Adaptar dicho return a las funciones que utilicen esta función
    """
    existe = list(coll_user.find({f"{search}": { "$eq": f"{name}" } }))
    if len(existe) == 0:
        return True
    else:
        return False


def chat(name):
    """
    Checkeamos si existe el chat en la base de datos.
    Devuelve TRUE si el chat NO EXISTE
    Adaptar return a las funciones que usen la función.
    """
    existe = list(coll_chat.find({"chat_name": { "$eq": f"{name}" } }))
    if len(existe) == 0:
        return True
    else:
        return False


def userInChat(chat,user):
    """
    Checkeamos si existe user en en el chat indicado.
    Necesita parámetros chat y usuario
    Devuelve True si está en el chat y False si el user no está en ese chat.
    """
    existe = list(coll_chat.find({ "chat_name" : f"{chat}", "participants" : f"{user}"}))
    if len(existe)== 0:
        return False
    else:
        return True


def message(message):
    """
    Checkea si el mensaje ya existe, para no tener mensajes duplicados.
    """
    existe = list(coll_message.find({ "message" : f"{message}"}))
    if len(existe)== 0:
        return False
    else:
        return True