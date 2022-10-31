import klasser
import Funksjoner

import csv
from datetime import datetime


def ny_avtale():
    temp_tittel = input("Hva er navnet på avtalen?")
    temp_sted = input("Hva er stedet til avtalen?")
    temp_starttidspunkt = ""
    while temp_starttidspunkt == "":
        try:
            temp_starttidspunkt = datetime(int(input("År:")),int(input("Måned:")),int(input("Dag:")),int(input("Time:")),int(input("Minutt:"))) 
        except ValueError:
            print("Ugyldig verdi! Prøv på nytt")

    temp_varighet = ""        
    while temp_varighet == "":
        try:     
            temp_varighet = int(input("Hvor lenge varer avtalen?"))
        except ValueError:
            print("Ugyldig verdi, prøv på nytt")

    return klasser.avtale(temp_tittel, temp_sted, temp_starttidspunkt, temp_varighet)

def utskrift_avtaler(list):
    for i in range(len(list)):
        print(i, list[i].Tittel, list[i])

def lage_fil_avtaler(list):
    doc = open ("avtaler.txt", "w", encoding="UTF-8")
    for i in range(len(list)):
        temp_str = F"{list[i].Tittel};{list[i].Sted};{list[i].Starttidspunkt};{list[i].Varighet} \n"
        doc.write(temp_str)
    doc.close()


#test
if __name__ == "__main__":
    list = list()

    for i in range(2):
        temp = Funksjoner.ny_avtale()
        list.append(temp)

    Funksjoner.utskrift_avtaler(list)
    Funksjoner.lage_fil_avtaler(list)