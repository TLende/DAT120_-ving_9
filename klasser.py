import datetime

class avtale:
    def __init__(self, tittel ="", sted ="", starttidspunkt="", varighet=0):
        self.Tittel = str(tittel)
        self.Sted = str(sted)
        self.Starttidspunkt = datetime.datetime.fromisoformat(starttidspunkt)
        self.Varighet = int(varighet)
