import Funksjoner
import klasser
import meny
from datetime import datetime

date = datetime.now()
liste_avtaler = []
liste_kategorier = []
liste_steder = []

#liste.append(klasser.avtale("Skule","uis",datetime.now(),20))
#liste.append(klasser.avtale("Test","Test2",datetime.now(),30))

if __name__ == "__main__":
    while True:
        menyl = [
            "   [1]Avtaler",
            "   [2]Sted",
            "   [3]Kategori",
            "   [7]Avslutt"
        ]
        menyv = [
            meny.menycommon("Avtaler",liste_avtaler),
            meny.menycommon("Sted",liste_steder),
            meny.menycommon("Kategori",liste_kategorier),
            quit
        ]
        print("Valgene er")
        for x in range(len(menyl)):
            print(menyl[x],end='\n')
        while True:
            tempi = input(f"Skriv inn valget her 1-{len(menyl)}: ")
            try:
                menyv[int(tempi)-1]()
                break
            except TypeError:
                menyv[int(tempi)-1](liste_avtaler)
                break
            except ValueError:
                print("Ikke gyldig verdi prøv igjen")