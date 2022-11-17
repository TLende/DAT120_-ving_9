import Funksjoner
import Oving_10
import klasser

def menycommon(type,list_avtale,list_sted,list_kategori):
    loop = True
    while loop == True:
        list = [list_avtale,list_sted,list_kategori]
        list1 = ["Avtale", "Sted", "Kategori"]
        for x in range(len(list)):
            if list1[x] == type:
                tlist = x
        menyc = [
            f"Skriv inn ny {type}",
            f"Les {type} fra fil",
            f"Skriv {type} til fil",
            f"Skriv ut alle {type}",
            f"Slett {type}",
            f"Rediger {type}",
            f"Legg til kategori til avtale",
            f"Søk etter avtaler med sted"
        ]
        menya = [
            Funksjoner.ny_avtale,
            Funksjoner.lese_fil_avtaler,
            Funksjoner.lage_fil_avtaler,
            Funksjoner.utskrift_klasser,
            Funksjoner.slett_fra_lite,
            Funksjoner.rediger_avtale,
            Funksjoner.legg_til_kategorier,
            Funksjoner.sted_sok
        ]
        menys = [
            Oving_10.nyttsted,
            Oving_10.lese_fil_sted,
            Funksjoner.lage_stedliste,
            Funksjoner.utskrift_klasser,
            Funksjoner.slett_fra_lite,
        ]
        menyk = [
            Oving_10.ny_kategori,
            Oving_10.lese_fil_sted,
            Funksjoner.lage_fil_kategori,
            Funksjoner.utskrift_klasser,
            Funksjoner.slett_fra_lite,
        ]
        meny = [menya,menys,menyk]
        menyv =["Avtale","Sted","Kategori"]
        tmeny = 0
        for x in range(len(menyv)):
            if type == menyv[x]:
                tmeny = x
        for x in range(len(meny[tmeny])):
            print(f"    [{x+1}]{menyc[x]}")
            if x == len(meny[tmeny])-1:
                print(f"    [{x+2}]Bekreft")
        while True:
            valg = int(input(f"Skriv in valget her 1-{len(meny[tmeny])+1}: "))-1
            try:
                if valg == len(meny[tmeny]):
                    loop = False
                else:
                    meny[tmeny][valg](list[tlist])
                break
            except klasser.Stederror:
                try:
                    meny[tmeny][valg](list[tlist],list_sted,True)
                except klasser.Stederror:
                    print("Lista er tom")
                break
            except klasser.kategorierror:
                try:
                    meny[tmeny][valg](list[tlist],list_kategori)
                except klasser.kategorierror:
                    print("Lista er tom")
                break
            except:
                print("Ikke gyldig verdi prøv igen")

if __name__ == "__main__":
    test = "Sted"

    menycommon(test)