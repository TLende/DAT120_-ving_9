def lese_fil(liste,variabel):
    lvariabel = list()
    if variabel == "Avtale":
        tvariabel = str(vars(klasser.avtale()))
    elif variabel == "Sted":
        tvariabel = str(vars(klasser.Sted()))
    elif variabel == "Kategori":
        tvariabel = str(vars(klasser.Kategori()))
    lvariabel = tvariabel.split(',').
    for x in range(len(lvariabel)):
        print(lvariabel[x])