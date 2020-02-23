from textblob import TextBlob
from statistics import mean
import emoji as em


def sentimientosMen(mensaje):
    """
    analiza la polaridad de positivo/negativo de una frase (o lista) y devuelve
    un diccionario con la media de los mensajes
    """
    polaridad = []
    subjetividad = []
    sentimientos = []
    if type(mensaje) != list:
        trad = TextBlob(f"{mensaje}")
        en = trad.translate(from_lang="es",to="en")
        print(f"mensaje traducido{en}")
        sentimientos.append(en.sentiment)
        for s in sentimientos:
            polaridad.append(s[0])
            subjetividad.append(s[1])
        arriba = (em.emojize(':thumbs_up:',use_aliases=True))
        abajo = (em.emojize(':thumbs_down:',use_aliases=True))
        emoji = [arriba if mean(polaridad) >=0 else abajo]

        dict_analisis = {"Frase": f"{mensaje}",
                         "polaridad": f"{mean(polaridad)}{emoji}",
                         "subjetividad": f"{mean(subjetividad)}"

                         }
    else:
        for m in mensaje:
            trad = TextBlob(f"{m}")
            en = trad.translate(from_lang="es",to="en")
            sentimientos.append(en.sentiment)
        
        for s in sentimientos:
            polaridad.append(s[0])
            subjetividad.append(s[1])
        arriba = (em.emojize(':thumbs_up:',use_aliases=True))
        abajo = (em.emojize(':thumbs_down:',use_aliases=True))
        emoji = [arriba if mean(polaridad) >=0 else abajo]

        dict_analisis = {"polaridad": f"{mean(polaridad)}{emoji}",
                         "subjetividad": f"{mean(subjetividad)}"
                         }
    return dict_analisis
