from curses import window
import tkinter as tk

def guimain():
    window = tk.Tk()
    Overskrift = tk.Label(text="Meny",font=("",15))
    Overskrift.pack()
    leggtil = tk.Button(text="Legg til avtale", )
    leggtil.pack()
    avtaleoversikt = tk.Button(text="Avtaleoversikt")
    avtaleoversikt.pack()
    avslutt = tk.Button(text="Avslutt")
    avslutt.pack()
    window.mainloop()

def guileggtil():
    window = tk.Tk()
    Overskrift = tk.Label(text="Legg til avtale",font=("",15))
    Overskrift.pack()
    Tittel = tk.Label(text="Tittel")
    TittelE = tk.Entry()
    Tittel.pack()
    TittelE.pack()
    Sted = tk.Label(text="Sted")
    StedE = tk.Entry()
    Sted.pack()
    StedE.pack()
    Tid = tk.Label(text="Tid")
    TidE = tk.Entry()
    TidB = tk.Button(text="Sett tid til nå")
    Tid.pack()
    TidE.pack()
    TidB.pack()
    Leggtil = tk.Button(text="Legg til")
    Leggtil.pack()
    Meny = tk.Button(text="Tilbake til meny")
    Meny.pack()
    window.mainloop()

def guiavtaleoversikt():
    window = tk.Tk()
    Overskrift = tk.Label(text="Avtaleoversikt",font=("",15))
    Overskrift.pack()
    with open("avtaler.txt", "r", encoding="UTF-8") as fil:
        for linje in fil:
            Teskst = tk.Label(text=linje.rstrip('\n'))
            Teskst.pack()
    Meny = tk.Button(text="Tilbake til meny")
    Meny.pack()
    window.mainloop()

if __name__ == "__main__":
    guiavtaleoversikt()
    guimain()
    guileggtil()