import klasser
import Funksjoner

def nyttsted():
    return klasser.Sted(input("StedID:"), input("Sted navn:"), input("gateadresse:"), int(input("postnr:")), input("poststed:"))


#Lager ny kategori
def ny_kategori():
    try:
        kategori_navn = input("Hva er navnet på kategorien?")
        kategori_id = input("Hva er id til kategorien?")
        kategori_prioritet = int(input("Hvor høy prioritet? Legg inn et tall mellom 1 og 3 der 1 er lite viktig og 3 er svært viktig."))
        return klasser.Kategori(kategori_id, kategori_navn, kategori_prioritet)
    except ValueError:
        print("Ikke gyldig, prøv igjen")
    
    return klasser.Kategori(kategori_navn, kategori_id, kategori_prioritet)
    
#Leser en fil "Navn; id; Prioritet", og lagrer  i liste
def lese_fil_kategori(list):
    try:
        doc = open(input("Skriv inn fil navn:"), "r", encoding="UTF-8")
        print("Her er kategoriene i fila:")
        for i in doc:
            try:
                print(i)
                data_split = i.strip().split(";")
                list.append(klasser.Kategori(data_split[0], data_split[1], data_split[2]))
            except:
                pass
    except:
        print("File not found.")

#Leser en fil "id;navn;gateadresse;postnr;poststed", og lagrer i liste
def lese_fil_sted(list):
    try:
        doc = open(input("Skriv inn fil navn:"), "r", encoding="UTF-8")
        print("Her er steda i fila:")
        for i in doc:
            try:
                print(i)
                data_split = i.strip().split(";")
                list.append(klasser.Sted(data_split[0], data_split[1], data_split[2], data_split[3], data_split[4]))
            except:
                pass
    except:
        print("File not found.")

if __name__ == "__main__":
    kategorier = []

    lese_fil_sted(kategorier)

    for i in range(len(kategorier)):
        print(kategorier[i])


    
    


