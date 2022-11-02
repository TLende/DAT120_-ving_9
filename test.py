import Funksjoner
import klasser

def liste(list,x,y):
    meny = [
        list[x].Tittel,
        list[x].Sted
    ]
    meny[y] = input("ok")
    
x=0
y=0
lister = list()

lister.append(klasser.avtale("Skule","uis",datetime.now(),20))

liste(lister,x,y)
print(lister[0])