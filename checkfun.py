from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/apidb")
db = client.get_database()
coll_user = db['users']
coll_chat = db['chats']


def user(name,search):
    existe = list(coll_user.find({f"{search}": { "$eq": f"{name}" } }))
    if len(existe) == 0:
        return True
    else:
        return False


def chat(name):
    existe = list(coll_chat.find({"chat_name": { "$eq": f"{name}" } }))
    if len(existe) == 0:
        return True
    else:
        return False