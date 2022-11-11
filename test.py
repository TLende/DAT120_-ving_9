import Funksjoner
import klasser
from datetime import datetime

class test(object):
    def __init__(self):
        self.tittel = 1
        self.verdi = 2

    def __str__(self):
        return self.tittel

lot = test
print(test())