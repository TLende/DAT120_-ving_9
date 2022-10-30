import klasser
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
