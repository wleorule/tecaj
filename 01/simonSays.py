import random
import time
import os

def ispisiIzbornik(): 
    print("Izbornik")
    print("1. Simon says")
    print("2. Memory")
    print("3. Krizic kruzic")
    print("4. Izlaz")

def simonSays():
     listaBrojeva = []
     nastaviIgru = True
     while nastaviIgru: 
        # 1. Generiraj novi broj i stavi ga u listu brojeva
        noviBroj = random.randint(1, 4)
        listaBrojeva.append(noviBroj)
        # 2. Ispisi sve brojeve iz liste
        for broj in listaBrojeva:
            print(broj)
            time.sleep(1)
        # 3.1 Očisti ekran tako da igrač ne vidi brojeve 
        os.system('clear') 
        # 3. Traži unos svih brojeva iz liste
        for broj in listaBrojeva:
            unosNovogBroja = input(": ")
            # 4. ako je broj dobar nastavi igru ako nije nemoj
            if int(unosNovogBroja) == broj:
                nastaviIgru = True
            else:
                print("izgubio si")
                nastaviIgru = False    
                break # Da nas izbaci iz igre (ne pita za unos više) ako smo izgubili, break će izači iz petlje prije nego je gotova     

# 1. Odabir karata ✅
# 2. Promjesaj karte ✅
# 3. Posloži plocu ✅
#   3.1. ispis prva 4, dodaj novi red 
#   3.2. ispis druga 4, dodaj novi red 
#   3.3. ispis trca 4, dodaj novi red 
#   3.4. ispis cetvrta 4, 

# 3. Dopusti igracu jedan da odabere dvije karte 
# 4. Provjeri karte ako su dobre makni ih s ploce ako nisu vrati natrag

# 5. Ako nema više što za birati igra je gotova 

karte = ["👋", "👋", "🤖", "🤖","💡","💡","😉","😉","🔥","🔥","👀","👀","🌍","🌍","🍺","🍺"]
promjesaneKarte = []
def promjesajKarte(): 
    uzetaKarta = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    while False in uzetaKarta: 
        novaKarta = random.randint(0, 15)
        if(uzetaKarta[novaKarta] == False): 
            promjesaneKarte.append(karte[novaKarta])
            uzetaKarta[novaKarta] = True

def ispisi(ploca): 
    os.system('clear') 
    for brojac in range(0,16): 
        print(ploca[brojac], end=" ")
        brojZaProvjeru = brojac + 1
        if brojZaProvjeru % 4 == 0:
            print("")

okrenutaKarta = "❓"
trenutnaIgra = [okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta,okrenutaKarta]

rezultat = [0,0]
trenutniIgrac = 0

def igrajMemory(): 
    ispisi(trenutnaIgra)
    prvaKarta = input("Odaberi prvu kartu: ")
    redPrveKarte = int(prvaKarta.split(".")[0])
    stupacPrveKarte = int(prvaKarta.split(".")[1])
    odabranaPrvaKarta = ((redPrveKarte - 1) * 4) + (stupacPrveKarte - 1)
    trenutnaIgra[odabranaPrvaKarta] = promjesaneKarte[odabranaPrvaKarta]
    ispisi(trenutnaIgra)
    
    drugaKarta = input("Odaberi drugu kartu: ")
    redDrugeKarte = int(drugaKarta.split(".")[0])
    stupacDrugeKarte = int(drugaKarta.split(".")[1])
    odabranaDrugaKarta = ((redDrugeKarte - 1) * 4) + (stupacDrugeKarte - 1)
    trenutnaIgra[odabranaDrugaKarta] = promjesaneKarte[odabranaDrugaKarta]
    ispisi(trenutnaIgra)
    time.sleep(1)
    if promjesaneKarte[odabranaDrugaKarta] == promjesaneKarte[odabranaPrvaKarta]:
        rezultat[trenutniIgrac] = rezultat[trenutniIgrac] + 1
        trenutnaIgra[odabranaDrugaKarta] = "✅"
        trenutnaIgra[odabranaPrvaKarta] = "✅"
    else: 
        trenutnaIgra[odabranaDrugaKarta] = "❓"
        trenutnaIgra[odabranaPrvaKarta] = "❓"
    igrajMemory()
    
    #red.stupac
    #3.2.split(".")
    #["3", "2"]



#   13 : 4 = 3 - Ostatak = 1
#   22 : 4 = 5 - Ostatak = 2
#   16 : 4 = 4 - Ostatak = 0
#   16 % 4 = 0 
#   22 % 4 = 2 
#

def memory(): 
    promjesajKarte()
    igrajMemory()


ispisiIzbornik()
izbor = input("Izbor: ")

if izbor == "1": 
    simonSays()
elif izbor == "2": 
    memory()
elif izbor == "3": 
    print("KK")







    