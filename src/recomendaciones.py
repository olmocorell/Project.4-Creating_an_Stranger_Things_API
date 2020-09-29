import checkfun as check
import mongoget as mgget
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
import numpy as np
import pandas as pd

users = mgget.users()
mensajes = [mgget.messagesUser(a.get("name")) for a in users]

def recomiendaUser(name):
    checkparam = "name" 
    if check.user(checkparam,name) == True:
        pass
    else:
        error = "El usuario no existe, indique uno existente o cree uno nuevo"
        raise ValueError(error)
    return recomendaciones(name)
    

def diccionarioGrande():
    """
    Esta función hace un diccionario con todos los users como key y sus
    frases (todas juntas) como values. Para las recomendaciones.
    """
    tuplas = []
    for locura in mensajes:
        key = [a.get("name") for a in locura]
        values = [a.setdefault("message") for a in locura]
        tuplas.append((key[0], " ".join(values)))
    return dict(tuplas)


def recomendaciones(name):
    docs = diccionarioGrande()
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(docs.values())
    m = sparse_matrix.todense()
    df = pd.DataFrame(m, columns=count_vectorizer.get_feature_names(),
                      index=docs.keys())
    similarity_matrix = distance(df,df)
    sim_df = pd.DataFrame(similarity_matrix, columns=docs.keys(), index=docs.keys())
    np.fill_diagonal(sim_df.values, 0)
    nombre = sim_df.idxmax()
    respuesta = {}
    respuesta[name] = f'Creo que conectas bastante bien con  {nombre.loc[name]}'
    return respuesta
