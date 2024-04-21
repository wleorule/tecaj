# 1. Odabir karata koje će igrati ( 8 parova = 16 karata)
# 2. Mješanje karata
# 3. Slaganje karata na stol, ali tako da budu sakrivene (4x4)
# 4. Igrač jedan odabire dvije karte
#
# Ako su karte iste uzima sebi kartu ako nisu okreće ih natrag da budu sakrivene
# Igra se završava kada nema više karata na stolu, pobjednik je onaj koji ima najviše osvojenih parova

###################

# 1. Odabrati karte koje će igrati (8 parova = 16 karata)
#    Za lice karta ćemo koristiti emotikone ["👋", "👋", "🤖", "🤖","💡","💡","😉","😉","🔥","🔥","👀","👀","🌍","🌍","🍺","🍺"]
#    Za leđa karata ćemo korisiti ❓

# 2. Radimo "algoritam" za mješanje karata
#    2.1. Odabiremo nasumičnu kartu s popisa karata
#    2.2. Ako se ta karta već nalazi na popisu promješanih karata ignoriramo ju i idemo birati ponovo
#    2.3. Ako se karta ne nalazi na popisu promješanih karata stavljamo je na kraj
#    NOTE: Morati ćemo imati još jednu listu koja će pratiti koje smo karte s popisa karata uzeli!

# 3. Ispisujemo popis promješanih karata
#    3.1. Ispisujemo jednog po jednog člana liste popisa promješanih karata U ISTOM REDU
#    3.2. Nakon svake četvrte karte želimo ići u novi red kako bi dobili 4 x 4 ploču

# 4. Igramo 
#    4.1. Igrač koji je na redu okreće kartu tako da unese kordinate karte koju želi odabrati u obliku <red>.<stupac> (primjerice 3.2)
#    4.2. Ispisujemo mu ploću s okrenutom kartom
#    4.3. Igrač koji je na redu okreće drugu kartu tako da unese kordinate karte koju želi odabrati u obliku <red>.<stupac> (primjerice 3.2)
#    4.4. Ispisujemo mu ploću s okrenutom kartom (sada su okrenute dvije karte)
#    4.5. Pričekamo malo da igrači imaju vremena zapamtiti karte
#    4.6. Provjerimo jesu li odabrane karte jednake ako jesu onda dodjelimo bod tom igraću i zamjenimo karte s ✅ kako bi igrači znali da je to polje već odabrano
#    4.7. Promjenimo igraća i igramo dok god ima karata za birati

mojaLista = [1,2,55,4,7]
print("\n\n")

#len(<lista>) -> Vraća koliko lista ima članova
print(len(mojaLista))
input("\n\n")

# lista.clear() -> Briše sve članove iz liste
print(mojaLista)
mojaLista.clear();
print(mojaLista)
input("\n\n")

# lista.append(<element>) -> Dodaje novi član NA KRAJ liste
print(mojaLista)
mojaLista.append(44)
mojaLista.append(34)
print(mojaLista)
mojaLista.append(8)
print(mojaLista)
input("\n\n")

# Modulo % -> Daje ostatak djeljenja 2 broja
# primjerice 12 % 4 = 0, 
print(12%4)
print(15%4)
print(15%3)
print(12%3)
print(10%3)
print(4%2)
input("\n\n")

# tekst.split("<separator>") -> Djeli tekst na manje komadiće prema određenom kriteriju. 
# separator označava znak koji će split tražiti i prema kojem će odvajati. 
# rezultat .split-a je LISTA 
# primjerice "L.E.O".split(".") -> ["L", "E", "O"]
print("Something is rotten in the state of Denmark.".split(" ")) #Odvojeno je po razmaku
print("To be, or not to be, that is the question.".split(",")) #Odvojeno je po zarezu
print("3.2".split("."))
input("\n\n")

# int("01") -> pretvara tekst u broj ("3" nije isto kao 3)
print(int("3"))
print(int("43"))
input("\n\n")

# Izrada naših naredbi (funkcija) 
# Gramatika: def <naziv funkije/naredbe>(<argumenti (varijable koje prosljeđujemo u naredbu)>): 
# Koristimo kako bi mogli određeni algoritam/kod izvesti više puta bez da ga moramo kopirati 
def izračunajPovršinuKruga(radius): 
    return radius * radius * 3.1415; 

def nacrtajKocku(visina, sirina): 
    for x in range(visina):
        znakZaKraj = "|"
        znakZaSredinu = " "

        if x == 0 or x == visina-1: 
            znakZaKraj = znakZaSredinu = "-"
        
        for y in range(sirina):
            if(y == 0 or y == sirina -1):
                print(znakZaKraj, end="")
            else: 
                print(znakZaSredinu, end="")
        print("")

# Pozivanje naredbe
print(izračunajPovršinuKruga(5))
print(izračunajPovršinuKruga(17))
print(izračunajPovršinuKruga(9))
input("\n\n")

nacrtajKocku(3,3)
input("\n\n")
nacrtajKocku(5,7)
input("\n\n")
nacrtajKocku(7,7)