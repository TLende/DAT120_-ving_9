from datetime import datetime

import Funksjoner
import klasser
import meny

date = datetime.now()
liste_avtaler = []
liste_kategorier = []
liste_steder = []
kuk= "ok"
1
#liste.append(klasser.avtale("Skule","uis",datetime.now(),20))
#liste.append(klasser.avtale("Test","Test2",datetime.now(),30))

if __name__ == "__main__":
    while True:
        list1 = ["Avtale","Sted","Kategori"]
        menyl = [
            "   [1]Avtaler",
            "   [2]Sted",
            "   [3]Kategori",
            "   [4]Avslutt"
        ]
        print(f"{liste_avtaler=}")
        print(f"{liste_steder=}")
        print(f"{liste_kategorier=}")
        print("Valgene er:")
        for x in range(len(menyl)):
            print(menyl[x])
        while True:
            tempi = int(input(f"Skriv inn valget her 1-{len(menyl)}: "))
            try:
                if tempi == 4:
                    quit
                meny.menycommon(list1[tempi-1],liste_avtaler,liste_steder,liste_kategorier)

                break
            except ValueError:
                print("Ikke gyldig verdi prøv igjen")
