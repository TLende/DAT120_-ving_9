import Funksjoner
import Oving_10

def menycommon(type,list):
    while True:
        menyc = [
            f"Les {type} fra fil",
            f"Skriv {type} til fil",
            f"Skriv inn ny {type}",
            f"Skriv ut alle {type}",
            f"Slett {type}",
            f"Rediger {type}",
        ]
        menya = [
            Funksjoner.ny_avtale,
            Funksjoner.lese_fil_avtaler,
            Funksjoner.lage_fil_avtaler,
            Funksjoner.utskrift_klasser,
            Funksjoner.slett_fra_lite,
            Funksjoner.rediger_avtale,
        ]
        menys = [
            Oving_10.nyttsted,
            Oving_10.lese_fil_sted,
            "placeholder fo lese fil",
            Funksjoner.utskrift_klasser,
            Funksjoner.slett_fra_lite,
        ]
        menyk = [
            Oving_10.ny_kategori,
            Oving_10.lese_fil_sted,
            "placeholder fo lese fil",
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
            print(f"[{x+1}]{menyc[x]}")
            if x == len(meny[tmeny])-1:
                print(f"[{x+2}]Bekreft")
        while True:
            valg = input(f"Skriv in valget her 1-{len(meny[tmeny])+1}: ")
            try:
                meny[tmeny][valg]()
                break
            except TypeError:
                meny[tmeny][valg](list)
                break
            except ValueError:
                print("Ikke gyldig verdi prøv igen")

if __name__ == "__main__":
    test = "Sted"

    menycommon(test)