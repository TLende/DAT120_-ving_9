# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:18:27 2022

@author: Thoma
"""


# Funksjon som finner avtaler på en gitt dato
def avtale_dato(navn_class,navn_returnert_class,dato):
    for tittel in navn_class:
        avtale = navn_class[tittel]
        avtale_dato = str(starttidspunkt)
        avtale_dato_liste = avtale_dato.split(" ")
        for tid in avtale_dato_liste:
            if dato == avtale_dato_liste[0]:
                navn_returnert_class[tittel] = avtale    
    return navn_returnert_class


# Funksjon som leter etter titler til avtaler i en streng
def avtale_tittel(navn_class,tittel_returnert_class, streng):
    for tittel in navn_class:
        avtale = navn_class[tittel]
        tittel_lower = tittel.lower()
        streng_lower = streng.lower()
        if streng_lower.find(tittel_lower) >= 0:
            tittel_returnert_class[tittel] = avtale
    return tittel_returnert_class
