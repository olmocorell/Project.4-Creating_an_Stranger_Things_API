![Portada](https://github.com/agalvezcorell/Project.4-Creating_an_Stranger_Things_API/blob/master/input/portada.jpg)

# Creando una API de Stranger Things
Analizando sentimientos de un chat con TextBlob y realizando recomendaciones con NLP (procesamiento del lenguaje natural) en Python.

En este proyecto he creado una API de Stranger Things que permite obtener información de una base de datos que contiene mensajes que se han enviado los personajes en sus grupos de mensajería.

### ¿Cómo funciona?

## @post

- Insertar personajes.
Se pueden insertar personajes en la base de datos realizando una request.post a la API como en el siguiente ejemplo. El sistema checkeará que no existan los personajes.

```user ={"name":"Mike Wheeler"}```
```url_user = "http://localhost:5000/new/user"```
``` requests.post(url_user, data=user)```
