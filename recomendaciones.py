from sklearn.feature_extraction.text import CountVectorizer
import conmongo as mg

users = mg.users()
mensajes = [mg.messagesUser(a.get("name")) for a in users]



def diccionarioGrande():
    tuplas = []
    for locura in mensajes:
        key = [a.get("name") for a in locura]
        values = [a.setdefault("message") for a in locura]
        tuplas.append((key[0], " ".join(values)))
    tup = dict(tuplas)
    print(tup)
    return "hola"

def recomiendaUser(name):
    
    """
    mensajesuser = mg.messagesUser(name)
    frases = [a.get("message") for a in mensajesuser]
    string = " ".join(frases)
    user1 = {"name": f"{name}",
    "mensajes":f"{string}"
    }
    """
    print(mensajes)
    return "hola"

