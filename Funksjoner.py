import klasser
import Funksjoner

from datetime import datetime

# Lager ny avtale
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

# Skriver ut avtaler i ei liste
def utskrift_avtaler(list):
    for i in range(len(list)):
        print(i, list[i].Tittel, list[i])

# Lager en fil med formatet: Tittel;Sted;Starttidspunkt;Varighet
def lage_fil_avtaler(list):
    doc = open ("avtaler.txt", "w", encoding="UTF-8")
    for i in range(len(list)):
        temp_str = F"{list[i].Tittel};{list[i].Sted};{list[i].Starttidspunkt};{list[i].Varighet} \n"
        doc.write(temp_str)
    doc.close()

# Funksjon som finner avtaler på en gitt dato
def avtale_dato(dato,list):
    print(F"Her er alle avtalene som har dato:{dato.date()}")
    return_str = ""
    for i in range(len(list)):
        temp_dato = list[i].Starttidspunkt.date()
        if temp_dato == dato.date():
            return_str += F"{list[i].Tittel}:{temp_dato} \n"
    return return_str
            
# Funksjon som leter etter titler til avtaler i en streng
def avtale_tittel(streng, list):
    print(F"Her er alle avtalene som har tittelen: {streng}")
    return_str = ""
    for i in range(len(list)):
        tittel_lower = list[i].Tittel.lower()
        streng_lower = streng.lower()
        if tittel_lower == streng_lower:
            return_str += F"{list[i].Tittel}:{list[i].Starttidspunkt}"
    return return_str

#test
if __name__ == "__main__":
    list = list()
    dato = datetime(2022,1,1,12,0)
    tittel = "test"

    list.append(klasser.avtale("Skule","uis",dato,20))
    list.append(klasser.avtale("Test","Test2",dato,30))
    
    print(Funksjoner.avtale_dato(dato, list))
    print(Funksjoner.avtale_tittel(tittel, list))

    Funksjoner.utskrift_avtaler(list)
    Funksjoner.lage_fil_avtaler(list)