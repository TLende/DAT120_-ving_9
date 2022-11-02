import Funksjoner
liste = [
    Funksjoner.stop,
    Funksjoner.lese_fil_avtaler
]
while True:
    if input("dada") == "ok":
        liste[0]()