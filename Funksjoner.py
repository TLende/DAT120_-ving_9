import klasser
import Funksjoner
import Oving_10

from datetime import datetime

# Lager ny avtale
def ny_avtale(list, sted_liste = [],liste_test = False):
    if liste_test == False and len(sted_liste) == 0:
        raise klasser.Stederror
    temp_tittel = input("Hva er navnet på avtalen?")
    x = input("Vil du velge et sted fra sted lista? y/n:")
    if x == "y" and len(sted_liste) != 0:
        print("Velg mellom disse:")
        for i in range(len(sted_liste)):
            print(F"{i}: {sted_liste[i]}")
        Index = int(input("Velg sted:"))
        temp_sted = sted_liste[Index]
    else:
        print("Legg til sted manuelt")
        temp_sted = klasser.Sted(input("Hva er ID:"),input("Hva er stedsnavnet:"))
        sted_liste.append(temp_sted)
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
    if len(list) == 0:
        print("Lista er tom")
    else:
        print("Skriver ut alle objektene i lista:")
        for i in range(len(list)):
            print(i+1, list[i].Tittel, list[i])

# Lager en fil
def lage_fil_avtaler(list):
    doc = open (input("Skriv inn ønsket navn på fil: "), "w", encoding="UTF-8")
    for i in range(len(list)):
        temp = ""
        for j in range(len(list[i].kategorier)):
            temp +=F"{list[i].kategorier[j].ID};{list[i].kategorier[j].Tittel};{list[i].kategorier[j].prioritet},"
        temp += F"{list[i].Sted.id};{list[i].Sted.Tittel};{list[i].Sted.gateadresse};{list[i].Sted.postnr};{list[i].Sted.poststed},"       
        temp += F"{list[i].Tittel};{list[i].Starttidspunkt};{list[i].Varighet} \n"
        doc.write(temp)
    doc.close()

# Leser in fil med formatet: Tittel;Sted;Starttidspunkt;Varighet og lagrer i liste
def lese_fil_avtaler(liste):
    while True:
        try:
            doc = open(input("Skriv inn fil navn: "), "r", encoding="UTF-8")
            print("Her er avtalene i fila:")
            for i in doc:
                try:
                    print(i)
                    temp_list = list()
                    data_split = i.strip().split(",")
                    x = int(len(data_split))
                    for j in range(x-2):
                        temp = data_split[j].strip().split(";")
                        _temp = klasser.Kategori(temp[0],temp[1], temp[2])
                        temp_list.append(_temp)
                    temp = data_split[x-2]
                    temp_sted = temp.strip().split(";")
                    _sted = klasser.Sted(temp_sted[0],temp_sted[1],temp_sted[2], temp_sted[3],temp_sted[4])
                    temp = data_split[x-1]
                    temp_avtale = temp.strip().split(";")
                    temp = klasser.avtale(temp_avtale[0], _sted, datetime.fromisoformat(temp_avtale[1]), temp_avtale[2])
                    for k in range(len(temp_list)):
                        temp.legg_til_kategori(temp_list[k])
                    liste.append(temp)
                    print("Blir lagra i lista")
                except:
                    pass
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

def slett_fra_lite(list):
    if len(list) == 0:
        print("Ingen avtaler lokalt")
    else:
        utskrift_klasser(list)
        while True:
            try:
                list.pop(int(input("Skriv inn tallet til avtalen som skal slettes: "))-1)
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

def legg_til_kategorier(list,list_kategori = list()):
    
    if len(list) != 0:
        if len(list_kategori) != 0:
            utskrift_klasser(list)
            try:
                x = int(input(f"Velg ønsket avtale 1-{len(list)}: "))-1
                if x in range(len(list)):
                        utskrift_klasser(list_kategori)
                        inputet = int(input(f"Velg kategori 1-{len(list_kategori)}: "))
                        print(f"Input:{inputet-1} og {range(len(list_kategori))}")
                        list[x].legg_til_kategori(list_kategori[inputet-1])
                else:
                    raise ValueError
            except klasser.brekreft:
                print("Ikke gyldig input prøv igjen")
        else:
            raise klasser.kategorierror

def sted_sok(list,list_sted = list(),liste_test = False):
    if len(list_sted) == 0 and liste_test == False:
        raise klasser.Stederror
    if len(list_sted) != 0:
        utskrift_klasser(list_sted)
        try:
            imp = int(input(f"Velg Sted 1-{len(list_sted)}: "))-1
            for x in list:
                print(list[x].Sted, list_sted[imp])
                if list[x].Sted == list_sted[imp]:
                    print(list[x])
        except:
            print("Ikke gyldig input")
    else:
        raise klasser.Stederror



#test av funksjoner
if __name__ == "__main__":
    avtaler = []
    kategorier = []
    Sted = []

    dato1 = datetime(2022,1,1,12,0)
    dato2 = datetime(2022,2,1,12,0)
    tittel = "test"
    kategorier.append(klasser.Kategori(1, "UiS", 1))
    kategorier.append(klasser.Kategori(2,"frisør", 3))
    Sted.append(klasser.Sted(1, "UiS", 6, 4360, "Varhaug"))

    #avtaler.append(klasser.avtale("test2",Sted[0],dato1,20))
    avtaler.append(klasser.avtale("Test",Sted[0],dato2,30))
    avtaler[0].legg_til_kategori(kategorier[0])
    avtaler[0].legg_til_kategori(kategorier[1])

    Funksjoner.ny_avtale(avtaler, Sted)

    #Funksjoner.lese_fil_avtaler(liste)

    #print(Funksjoner.avtale_dato(dato1, liste))
    #print(Funksjoner.avtale_tittel(tittel, liste))

    #Funksjoner.utskrift_avtaler(liste)
    #Funksjoner.lage_fil_avtaler(avtaler)
    #Funksjoner.lese_fil_avtaler(avtaler)