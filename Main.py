import Funksjoner
import klasser
from datetime import datetime

date = datetime.now()
liste = list()

#liste.append(klasser.avtale("Skule","uis",datetime.now(),20))
#liste.append(klasser.avtale("Test","Test2",datetime.now(),30))

if __name__ == "__main__":
    while True:
        menyl = [
            "   [1]Les avtaler fra fil",
            "   [2]Skriv avtaler til fil",
            "   [3]Skriv inn ny avtale",
            "   [4]Skriv ut alle avtaler",
            "   [5]Slett en avtale",
            "   [6]Rediger avtale",
            "   [7]Avslutt"
        ]
        menyv = [
            Funksjoner.lese_fil_avtaler,
            Funksjoner.lage_fil_avtaler,
            Funksjoner.ny_avtale,
            Funksjoner.utskrift_klasser,
            Funksjoner.slett_avtale,
            Funksjoner.rediger_avtale,
            quit
        ]
        print("Valgene er")
        for x in range(len(menyl)):
            print(menyl[x],end='\n')
        while True:
            tempi = input("Skriv inn valget her 1-7: ")
            try:
                menyv[int(tempi)-1]()
                break
            except TypeError:
                menyv[int(tempi)-1](liste)
                break
            except ValueError:
                print("Ikke gyldig verdi prøv igjen")