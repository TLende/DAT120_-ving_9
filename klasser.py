from datetime import datetime
from logging import exception
import Funksjoner
import Oving_10
import klasser

class avtale:
    def __init__(self, tittel ="", sted = "",starttidspunkt = datetime.now(), varighet=0):
        self.Tittel = str(tittel)
        self.Sted = sted
        self.Starttidspunkt = starttidspunkt
        self.Varighet = int(varighet)
        self.kategorier = []

    def __str__(self):
        return f"Avtale:{self.Tittel}, Sted:{self.Sted}, Tid:{self.Starttidspunkt}, og varer:{self.Varighet} min. Avtalen har kategoriene: {self.kategorierString()}"

    def kategorierString(self):
        result = ""
        for kategori in self.kategorier:
            result += f" navn: {kategori.Tittel} id: {kategori.ID}"
        return result

    def legg_til_kategori(self, kategori):
        self.kategorier.append(kategori)
        
        #Lager klasse "Kategori"
class Kategori:
    def __init__(self, ID=0, Tittel="", prioritet=1):
        self.Tittel = str(Tittel)
        self.ID = int(ID)
        self.prioritet = int(prioritet)
        
    def __str__(self):
        return f"Navn:{self.Tittel}, ID:{self.ID}, Prioritet:{self.prioritet}"

class Sted:
    def __init__(self, ID=0, navn="", gateadresse=0, postnr=0, poststed=""):
        self.id = int(ID)
        self.Tittel = str(navn)
        self.gateadresse = int(gateadresse)
        self.postnr = int(postnr)
        self.poststed = str(poststed)


    def __str__(self):
        return f"ID: {self.id}, Navn: {self.Tittel}, Gateadresse: {self.gateadresse}, Postnr: {self.postnr}, Poststed: {self.poststed}"

class brekreft(Exception): pass

class kategorierror(Exception): pass

class Stederror(Exception): pass