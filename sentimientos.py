from textblob import TextBlob
from statistics import mean

def sentimientosMen(mensaje):
    """
    analiza la polaridad de positivo/negativo de una frase (o lista) y devuelve
    un diccionario con la media de los mensajes
    """
    polaridad = []
    subjetividad = []
    sentimientos = []
    for m in mensaje:
        trad = TextBlob(f"{m}")
        en = trad.translate(from_lang="es",to="en")
        sentimientos.append(en.sentiment)
    
    for s in sentimientos:
        polaridad.append(s[0])
        subjetividad.append(s[1])

    dict_analisis = { "polaridad":f"{mean(polaridad)}",
    "subjetividad":f"{mean(subjetividad)}"

    }
    return dict_analisis