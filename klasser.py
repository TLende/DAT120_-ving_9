from datetime import datetime
import Funksjoner

class avtale:
    def __init__(self, tittel ="", sted ="",starttidspunkt = datetime.now(), varighet=0):
        try:
            self.Tittel = str(tittel)
            self.Sted = str(sted)
            self.Starttidspunkt = starttidspunkt
            self.Varighet = int(varighet)
        except ValueError:
            print("Ikke gyldig data, prøv igjen")

    def __str__(self):
        return f"Avtale:{self.Tittel}, Sted:{self.Sted}, Tid:{self.Starttidspunkt}, og varer:{self.Varighet} min"
class Sted:
    def __init__(self, ID, navn, gateadresse, postnr, poststed ):
        self.id = ID
        self.Tittel = navn
        self.gateadresse = gateadresse
        self.postnr = postnr
        self.poststed = poststed

    def __str__(self):
        return f"ID: {self.id}, Navn: {self.Tittel}, Gateadresse: {self.gateadresse}, Postnr: {self.postnr}, Poststed: {self.poststed}"
