from datetime import datetime

class avtale:
    def __init__(self, tittel ="", sted ="", starttidspunkt= datetime.now(), varighet=0):
        try:
            self.Tittel = str(tittel)
            self.Sted = str(sted)
            self.Starttidspunkt = starttidspunkt
            self.Varighet = int(varighet)
        except ValueError:
            print("Ikke gyldig data, prøv igjen")

    def __str__(self):
        return f"Avtale:{self.Tittel}, Sted:{self.Sted}, klokken:{self.Starttidspunkt}, og varer:{self.Varighet} min"
