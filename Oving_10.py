#Lager klasse "Kategori"
class Kategori:
    def __init__(self, ID="", navn="", prioritet=1):
        try:
            self.ID = str(ID)
            self.Tittel = str(navn)
            self.prioritet = str(prioritet)
        except ValueError:
            print ("Ikke gyldig, prøv igjen")
        
    def __str__(self):
        return f"Navn:{self.Tittel}, ID:{self.ID}, Prioritet:{self.prioritet}"

#Lager ny kategori
def ny_kategori():
    try:
        kategori_navn = input("Hva er navnet på kategorien?")
        kategori_id = input("Hva er id til kategorien?")
        kategori_prioritet = int(input("Hvor høy prioritet? Legg inn et tall mellom 1 og 3 der 1 er lite viktig og 3 er svært viktig."))
        return Kategori(kategori_id, kategori_navn, kategori_prioritet)
    except ValueError:
        print("Ikke gyldig, prøv igjen")
    
    return (a(kategori_navn, kategori_id, kategori_prioritet))

    
#Lager en fil "Navn; id; Prioritet"
def lage_fil_kategori(list):
    doc = open (input("Skriv inn ønsket navn på fil: "), "w", encoding="UTF-8")
    for i in range(len(list)):
        kategori_str = F"{list[i].Tittel};{list[i].ID};{list[i].prioritet}\n"
        doc.write(kategori_str)
    doc.close()

if __name__ == "__main__":
    liste = list()
    liste.append(ny_kategori())
    x=Kategori
    a=lage_fil_kategori(liste)

