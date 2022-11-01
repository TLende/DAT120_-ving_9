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
    Teskst = tk.Label(text="")
    TeskstE = tk.Entry()
    Teskst.pack()
    TeskstE.pack()
    Leggtil = tk.Button(text="Legg til")
    Leggtil.pack()
    window.mainloop()

def guiavtaleoversikt():
    window = tk.Tk()
    Overskrift = tk.Label(text="Avtaleoversikt",font=("",15))
    Overskrift.pack()
    with open("avtaler.txt", "r", encoding="UTF-8") as fil:
        for linje in fil:
            Teskst = tk.Label(text=linje.rstrip('\n'))
            Teskst.pack()
    window.mainloop()

if __name__ == "__main__":
    guiavtaleoversikt()
    guimain()
    guileggtil()