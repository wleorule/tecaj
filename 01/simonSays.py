import random
import time
import os

print("Izbornik")
print("1. Simon says")
print("2. Memory")
print("3. Krizic kruzic")
print("4. Izlaz")
izbor = input("Izbor: ")

if izbor == "1": 
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
elif izbor == "2": 
    print("Memory")
elif izbor == "3": 
    print("KK")







    