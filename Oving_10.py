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
    
#Lager en fil "Navn; id; Prioritet"
def lage_fil_kategori(list):
    doc = open (input("Skriv inn ønsket navn på fil: "), "w", encoding="UTF-8")
    for i in range(len(list)):
        kategori_str = F"{list[i].Tittel};{list[i].ID};{list[i].prioritet}\n"
        doc.write(kategori_str)
    doc.close()


def lage_stedliste(list):
    doc = open (input("Skriv inn ønsket navn på fil: "), "w", encoding="UTF-8")
    for i in range(len(list)):
        temp_str = F"{list[i].ID};{list[i].Tittel};{list[i].gateadresse};{list[i].postnr};{list[i].poststed} \n"
        doc.write(temp_str)
    doc.close()
