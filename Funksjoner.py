import klasser
import Funksjoner

from datetime import datetime

# Lager ny avtale
def ny_avtale(list):
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

    list.append(klasser.avtale(temp_tittel, temp_sted, temp_starttidspunkt, temp_varighet))

# Skriver ut avtaler i ei liste
def utskrift_klasser(list):
    print("Skriver ut alle avtalene i lista:")
    for i in range(len(list)):
        print(i, list[i].Tittel, list[i])

# Lager en fil med formatet: Tittel;Sted;Starttidspunkt;Varighet
def lage_fil_avtaler(list):
    doc = open (input("Skriv inn ønsket navn på fil: "), "w", encoding="UTF-8")
    for i in range(len(list)):
        temp_str = F"{list[i].Tittel};{list[i].Sted};{list[i].Starttidspunkt};{list[i].Varighet} \n"
        doc.write(temp_str)
    doc.close()

# Leser in fil med formatet: Tittel;Sted;Starttidspunkt;Varighet og lagrer i liste
def lese_fil_avtaler(list):
    while True:
        try:
            doc = open(input("Skriv inn fil navn: "), "r", encoding="UTF-8")
            print("Her er avtalene i fila:")
            for i in doc:
                try:
                    print(i)
                    data_split = i.split(";")
                    list.append(klasser.avtale(data_split[0], data_split[1], datetime.fromisoformat(data_split[2]), data_split[3]))
                except:
                    pass
                print("Blir lagra i lista")
            break
        except:
            print("File not found or error")

# Funksjon som finner avtaler på en gitt dato
def avtale_dato(dato,list):
    print(F"Her er alle avtalene som har dato:{dato.date()}")
    return_str = ""
    for i in range(len(list)):
        temp_dato = list[i].Starttidspunkt.date()
        if temp_dato == dato.date():
            return_str += F"{list[i].Tittel}:{temp_dato} \n"
    return return_str
            
# Funksjon som leter etter tittler til avtaler i en streng
def avtale_tittel(streng, list):
    print(F"Her er alle avtalene som har tittelen: {streng}")
    return_str = ""
    for i in range(len(list)):
        tittel = list[i].Tittel
        if tittel.lower() == streng.lower():
            return_str += F"{list[i].Tittel}:{list[i].Starttidspunkt} \n"
    return return_str

def slett_avtale(list):
    if len(list) == 0:
        print("Ingen avtaler lokalt")
    else:
        utskrift_klasser(list)
        while True:
            try:
                list.pop(int(input("Skriv inn tallet til avtalen som skal slettes: ")))
                break
            except:
                print("Ikke gyldig input")

def rediger_avtale(list):
    if len(list) == 0:
        print("Ingen avtaler å redigere")
    else:
        utskrift_klasser(list)
        while True:
            tempi = int(input("Skriv inn tallet til avtalen som skal redigeres: "))
            try:
                print(f"Valgt Avtale er : {list[tempi]}")
                while True:
                    meny = [
                        "   [1]Rediger Tittel",
                        "   [2]Rediger Sted",
                        "   [3]Rediger Starttidspunkt",
                        "   [4]Rediger Varighet",
                        "   [5]Bekreft"
                    ]
                    menyf = [
                        Rtittel,
                        Rsted,
                        Rstartstidspunkt,
                        Rvarigjet,
                        Rbekreft
                    ]
                    print("Valgene er:")
                    for x in range(len(meny)):
                        print(meny[x])
                    try:
                        menyf[int(input("Skriv inn valget her 1-5: "))-1](list,tempi)
                    except klasser.brekreft:
                        break
                    except:
                        print("Ikke gyldig verdi prøv igjen") 
                break 
            except:
                print("Ikke gyldig input")

def Rtittel(list,x):
    print(f"Nåværende Tittel: {list[x].Tittel}")
    list[x].Tittel = input("Ny Tittel:")
def Rsted(list,x):
    print(f"Nåværende Sted: {list[x].Sted}")
    list[x].Sted = input("Nytt Sted:")
def Rstartstidspunkt(list,x):
    print(f"Nåværende startstidspunkt: {list[x].Startstidspunkt}")
    while True:
        try:
            print("Nytt startstidspunkt: ", end="")
            list[x].Startstidspunkt = datetime(int(input("År:")),int(input("Måned:")),int(input("Dag:")),int(input("Time:")),int(input("Minutt:")))
            break
        except ValueError:
            print("Ugyldig verdi! Prøv på nytt")
def Rvarigjet(list,x):
    print(f"Nåværende varighet: {list[x].Varighet}")
    while True:
        try:
            list[x].Varighet = int(input("Ny varighet: "))
            break
        except ValueError:
            print("Ugyldig verdi! Prøv på nytt")
def Rbekreft(list,x):
    print(f"Ny avtale: {list[x]}")
    raise klasser.brekreft
    

def rediger_avtale_element(x, list):
    list[x] = Funksjoner.ny_avtale(list)

#test av funksjoner
if __name__ == "__main__":
    list = list()
    dato1 = datetime(2022,1,1,12,0)
    dato2 = datetime(2022,2,1,12,0)
    tittel = "test"

    list.append(klasser.avtale("test2","uis",dato1,20))
    list.append(klasser.avtale("Test","Test2",dato2,30))
    
    Funksjoner.lese_fil_avtaler(list)

    print(Funksjoner.avtale_dato(dato1, list))
    print(Funksjoner.avtale_tittel(tittel, list))


    Funksjoner.utskrift_klasser(list)
    Funksjoner.lage_fil_avtaler(list)