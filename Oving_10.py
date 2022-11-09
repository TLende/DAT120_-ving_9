def nyttsted():
    return Sted(input("StedID:"), input("Sted navn:"), input("gateadresse:"), int(input("postnr:")), input("poststed:"))

def lage_stedliste(list):
    doc = open (input("Skriv inn ønsket navn på fil: "), "w", encoding="UTF-8")
    for i in range(len(list)):
        temp_str = F"{list[i].ID};{list[i].Tittel};{list[i].gateadresse};{list[i].postnr};{list[i].poststed} \n"
        doc.write(temp_str)
    doc.close()

if __name__ == "__main__":
    liste = list()
    liste.append (nyttsted())
    print(liste[0])