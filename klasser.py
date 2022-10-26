import datetime

class avtale:
    def __init__(self, tittel ="", sted ="", starttidspunkt="", varighet=0):
        Tittel = str(tittel)
        Sted = str(sted)
        Starttidspunkt = datetime.datetime.fromisoformat(starttidspunkt)
        Varighet = int(varighet)
