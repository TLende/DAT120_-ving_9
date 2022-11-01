import Funksjoner
import klasser
from datetime import datetime

date = datetime.now()
liste = list()

liste.append(klasser.avtale("Skule","uis",datetime.now(),20))
liste.append(klasser.avtale("Test","Test2",datetime.now(),30))

if __name__ == "__main__":
    while True:
        menyl = [
            "   [1]Les avtaler fra fil"
            "   [2]Skriv avtaler fra fil"
            "   [3]Skriv inn ny avtale"
            "   [4]Skriv ut alle avtaler"
            "   [5]Avslutt"
        ]
        menyv = [
            Funksjoner.lage_fil_avtaler,
            Funksjoner.lese_fil_avtaler,
            Funksjoner.ny_avtale,
            Funksjoner.utskrift_avtaler,
            Funksjoner.stop
        ]
        print("Valgene er")
        for x in range(len(menyl)):
            print(menyl[x],end='\n')
        while True:
            try:
                menyv[int(input("Skriv inn valget her 1-5: "))-1]()
                break
            except TypeError:
                menyv[int(input("Skriv inn valget her 1-5: "))-1](liste)
                break
            except:
                print("Ikke gyldig verdi prøv igjen")