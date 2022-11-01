import Funksjoner
import klasser
from datetime import datetime

list = list()


list.append(klasser.avtale("Skule","uis",datetime.now(),20))
list.append(klasser.avtale("Test","Test2",datetime.now(),30))



Funksjoner.utskrift_avtaler(list)