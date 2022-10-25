class Land:
    def __init__(self, navn_IO, befolkning_IO="Ikke satt", areal_IO="Ikke satt"):
        self.navn = navn_IO
        self.befolkning = befolkning_IO
        self.areal = areal_IO

    def __str__(self):
        return f"Navn: {self.navn}, Befolkning: {self.befolkning} og Areal:{self.areal}"

    def befolkningstetthet(self):
        return float(float(self.befolkning) / float(self.areal))

def hoyest_befolkning(land1, land2):
    if int(land1.befolkning) < int(land2.befolkning):
        return print(f"{land2.navn} har størst befolkning")
    
    else:
        return print(f"{land1.navn} har størst befolkning")

if __name__ == "__main__":    
    dic = dict()
    file1 = open("befolkning_tabell_csv.txt", "r", encoding="UTF-8")
    file2 = open("areal_tabell_csv.txt", "r", encoding="UTF-8")

    for linje in file1:
        data_split = linje.strip().split(";")
        dic[data_split[0]] = Land(data_split[0], data_split[1])

    for linje in file2:
        data_split = linje.strip().split(";")
        if data_split[0] in dic:
            dic[data_split[0]].areal = data_split[1]

        else:
            print(f"{data_split[0]} er ikke i biblioteket")

    Highest_density = 0.0
    highest_density_country = ""
    for i in dic:
        if dic[i].areal != "Ikke satt" and dic[i].befolkning != "Ikke satt":
            print(dic[i])
            print(f"{dic[i].befolkningstetthet()} er befolkningstettheten til {dic[i].navn}")
            print("\n")

            if dic[i].befolkningstetthet() > Highest_density:
                Highest_density = dic[i].befolkningstetthet()
                highest_density_country = dic[i].navn
        else:
            print(f"{dic[i].navn} har ikke sett areal")
            print("\n")

    print(f"{highest_density_country} har størst befolkningstetthet på: {Highest_density}")