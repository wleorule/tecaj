import random
import os 
import time

karte = ["👋", "👋", "🤖", "🤖","💡","💡","😉","😉","🔥","🔥","👀","👀","🌍","🌍","🍺","🍺"]
popisPromjesanihKarata = []

def promjesajKarte():
    popisPromjesanihKarata.clear()
    uzeteKarte = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    while len(popisPromjesanihKarata) != 16:
        broj = random.randint(0,15)
        if uzeteKarte[broj] == False: 
            popisPromjesanihKarata.append(karte[broj])
            uzeteKarte[broj] = True

def ispis(popisKarata): 
    os.system('clear') # cls
    brojac = 1; 
    for karta in popisKarata:
        print(karta, end=" ")
        if brojac % 4 == 0: 
            print("")
        brojac = brojac + 1
        
def igrajMemory(): 
    promjesajKarte()
    spil = ["❓","❓","❓","❓","❓","❓","❓","❓","❓","❓","❓","❓","❓","❓","❓","❓"]
    trenutniIgrac = 0
    rezultat = [0,0]

    while "❓" in spil: 
        ispis(spil)

        print("")
        print("Igrac 1:" + str(rezultat[0]))
        print("Igrac 2:" + str(rezultat[1]))

        kordinate1Karte = input("Odaberi prvu kartu: ") # <red>.<stupac> 2.3 ["2", "3"]
        red1 = int(kordinate1Karte.split(".")[0])
        stupac1 = int(kordinate1Karte.split(".")[1])
        karta1 = (red1 - 1) * 4 + stupac1 - 1
        spil[karta1] = popisPromjesanihKarata[karta1]
        ispis(spil)
        kordinate2Karte = input("Odaberi drugu kartu: ") # <red>.<stupac> 2.3 ["2", "3"]
        red2 = int(kordinate2Karte.split(".")[0])
        stupac2 = int(kordinate2Karte.split(".")[1])
        karta2 = (red2 - 1) * 4 + stupac2 - 1
        spil[karta2] = popisPromjesanihKarata[karta2]
        ispis(spil)
        time.sleep(2)

        if popisPromjesanihKarata[karta1] == popisPromjesanihKarata[karta2]: 
            rezultat[trenutniIgrac] = rezultat[trenutniIgrac] + 1
            spil[karta1] = "✅"
            spil[karta2] = "✅"
        else: 
            spil[karta1] = "❓"
            spil[karta2] = "❓"
        
        if trenutniIgrac == 0: 
            trenutniIgrac = 1
        else:
            trenutniIgrac = 0



# 🍺 🤖 💡 👋 🌍 🔥 👀 😉 🤖 🍺 🌍 💡 🔥 👀 👋 😉 

# 🍺 🤖 💡 👋 
# 🌍 🔥 👀 😉 
# 🤖 🍺 🌍 💡 
# 🔥 👀 👋 😉 

# 2 * 4 = 8 + 3 = 11  
# red - 1 * 4 + stupac = X
# 3 - 1 = 2 * 4 = 8 + 3 = 11 - 1 = 10
igrajMemory()


