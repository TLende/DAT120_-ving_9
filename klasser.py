from datetime import datetime
import Funksjoner
import Oving_10
import klasser

class avtale:
    def __init__(self, tittel ="", sted = "",starttidspunkt = datetime.now(), varighet=0):
        try:
            self.Tittel = str(tittel)
            self.Sted = sted
            self.Starttidspunkt = starttidspunkt
            self.Varighet = int(varighet)
            self.kategorier = list()
        except ValueError:
            print("Ikke gyldig data, prøv igjen")

    def __str__(self):
        return f"Avtale:{self.Tittel}, Sted:{self.Sted}, Tid:{self.Starttidspunkt}, og varer:{self.Varighet} min. Avtalen har kategoriene: {self.kategorierString()}"

    def kategorierString(self):
        result = ""
        for kategori in self.kategorier:
            result = result + f" navn: {kategori.Tittel} id: {kategori.ID}"
        return result

    def legg_til_kategori(self, kategori):
        self.kategorier.append(kategori)
        
        #Lager klasse "Kategori"
class Kategori:
    def __init__(self, ID="", navn="", prioritet=1):
        try:
            self.ID = int(ID)
            self.Tittel = str(navn)
            self.prioritet = int(prioritet)
        except ValueError:
            print ("Ikke gyldig, prøv igjen")
        
    def __str__(self):
        return f"Navn:{self.Tittel}, ID:{self.ID}, Prioritet:{self.prioritet}"

class Sted:
    def __init__(self, ID, navn, gateadresse, postnr, poststed ):
        try:
            self.id = int(ID)
            self.Tittel = str(navn)
            self.gateadresse = int(gateadresse)
            self.postnr = int(postnr)
            self.poststed = str(poststed)
        except ValueError:
            print("Ikke gyldig, prøv igjen")

    def __str__(self):
        return f"ID: {self.id}, Navn: {self.Tittel}, Gateadresse: {self.gateadresse}, Postnr: {self.postnr}, Poststed: {self.poststed}"

