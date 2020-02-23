![Portada](https://github.com/agalvezcorell/Project.4-Creating_an_Stranger_Things_API/blob/master/input/portada.jpg)

# Creando una API de Stranger Things
Analizando sentimientos de un chat con TextBlob y realizando recomendaciones con NLP (procesamiento del lenguaje natural) en Python.

En este proyecto he creado una API de Stranger Things que permite obtener información de una base de datos que contiene mensajes que se han enviado los personajes en sus grupos de mensajería.

### ¿Cómo funciona?

## @post

- /new/user

Se pueden insertar personajes en la base de datos realizando una request.post a la API como en el siguiente ejemplo. El sistema checkeará que no existan los personajes.

```
user ={"name":"Mike Wheeler"}
url = "http://localhost:5000/new/user"
requests.post(url, data=user)
```
- /new/chat

Se pueden insertar chats utilizando este comando. Necesitas tener los datos en forma de diccionario.
```
chat = { "chat_name": "friends",
           "participants": ["Mike Wheeler","Dustin Henderson","Will","Lucas"]
}
url = "http://localhost:5000/new/chat"
requests.post(url_chat, data=dchat)
```
- /new/message

De esta manera insertamos un mensaje en la base de datos. 
```
mensaje = {'name': 'Once', 'chat_name': 'friends_new', 'message': 'Los amigos no mienten'}
url = "http://localhost:5000/new/message"
requests.post(url, data=mensaje)
```
## @get

- /users

Con este endpoint obtenemos todos los usuarios.
```
url = "http://localhost:5000/users"
requests.get(url).json()
```
- /chats

Con este endpoint podemos saber todos los grupos que hay creados
```
url = "http://localhost:5000/chats"
requests.get(url).json()
```
- /user/chat/name

Con este endopoint obtenemos los chats en los que participa el usuario que le indiquemos.
```
url_chats = "http://localhost:5000/user/chat/"
name = "Mike Wheeler"
requests.get(url_chats + name).json()
```
- /user/message/name

Con este endpoint obtenemos todos los mensajes que ha escrito un usuario.
```
url = "http://localhost:5000/user/message/"
name = "Once"
requests.get(url + name).json()
```
- /chat/message/name

Con este endpoint obtenemos todos los mensajes que se han escrito en un chat.
```
url = "http://localhost:5000/chat/message/"
grupo = "hawkins"
requests.get(url + grupo).json()
```

## Análisis de sentimientos
Con requests a la API podemos analizar los sentimientos de los mensajes que se han escrito en un chat, los sentimientos de una frase random de un usuario o de todos los mensajes de un usuario para saber si se expresa feliz o triste.

- /chat/sentiments/name

Analizamos la polaridad y subjetividad de los mensajes de este chat.
```
url = "http://localhost:5000/chat/sentiments/"
grupo =  "hawkins"
requests.get(url_sentchat + grupo2).json()
```
- /user/sentiments/name

Con este comando analizamos la polaridad y subjetividad de los mensajes de un usuario.
```
url = "http://localhost:5000/user/sentiments/"
dustin ="Dustin Henderson"
requests.get(url + dustin).json()
```
- /user/random/sentiments/name

Elegimos un usuario y el sistema nos devuelve el análisis de sentimientos de un mensaje elegido de forma aleatoria de entre todos los mensajes que ha escrito.
```
url= "http://localhost:5000/user/random/sentiments/"
hopper =  "Jim Hopper"
requests.get(url + hopper).json()
```
## Sistema de recomendaciones (NLP)
Mediante el procesado de lenguaje realizamos un sistema de recomendaciones basado en la temática de la que habla cada usuario.
En este caso, para obtener una recomendación de amistad, introduces un nombre en la request como en el siguiente ejemplo.
```
url= "http://localhost:5000/recommend/"
name = "Kali"
requests.get(url + name).json()
```