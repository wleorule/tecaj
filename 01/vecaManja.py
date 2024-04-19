import random
import os

# True/False da while zna kada treba stat s igrom
nastaviIgru = True

# Popis brojeva koji su prikazani
popisBrojeva = []
# Dodajemo broj na popis brojeva kako bi mogli odmah prikazati jedan broj
popisBrojeva.append(random.randint(0,9))

# While petlja tako da se igra nastavlja za stalno
while nastaviIgru: 
    # Očisti sve ispisano u prozoru Windows = CLS, Linux/Macos = CLEAR 
    os.system('clear') 
    noviBroj = random.randint(0,9)
    rezultat = "I"
    # Dohvati zadnji broj s liste brojeva (prvi put će to biti broj dodan na liniji 10)
    # "len()" nam vraća koliko ima brojeva u listi, mi oduzimamo 1 od tog broja pošto lista kreće od 0
    zadnjiBroj = popisBrojeva[len(popisBrojeva)-1] 
    if(noviBroj > zadnjiBroj): 
        rezultat = "V"
    elif(noviBroj < zadnjiBroj): 
        rezultat = "M"
    
    for broj in popisBrojeva: 
        print(broj, end=" ")
    print("")
    unos = input("(V/M/I): ")

    if(unos != rezultat): 
        print("Broj je bio: " + str(noviBroj) + " - " + rezultat)
        nastaviIgru=False
    else: 
        popisBrojeva.append(noviBroj)
print("SCORE:" + str(len(popisBrojeva)))
