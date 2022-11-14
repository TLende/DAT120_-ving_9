from datetime import datetime

import Funksjoner
import klasser
import meny

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
        print(test)