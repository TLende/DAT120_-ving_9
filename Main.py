import Funksjoner
import klasser
from datetime import datetime

list = list()

#list.append(klasser.avtale("Skule","uis",datetime.now(),20))
#list.append(klasser.avtale("Test","Test2",datetime.now(),30))

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
            print("placeholder"),
            print("placeholder"),
            Funksjoner.ny_avtale,
            Funksjoner.utskrift_avtaler,
            print("placeholder")
        ]
        print("Valgene er")
        for x in range(len(menyl)):
            print(menyl[x],end='\n')

        menyv[int(input("Skriv inn valget her 1-5: "))-1]
    