from pymongo import MongoClient
import checkfun as check
from bson.json_util import dumps
import re
client = MongoClient("mongodb://localhost:27017/apidb")
db = client.get_database()
coll_user = db['users']
coll_chat = db['chats']


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