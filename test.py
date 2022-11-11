import Funksjoner
import klasser
from datetime import datetime

class test(object):
    def __init__(self,g,h):
        self.tittel = g
        self.verdi = h

    def __str__(self):
        return self.tittel

lot = test
print(vars(test()))