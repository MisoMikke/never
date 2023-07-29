import random
with open('neverever.txt', 'r') as file:
    kysymys = file.readlines()
print("Tervetuloa pelaamaan never have I ever -peliä!")
print("Aloittaaksesi pelin, kirjoita 'aloita'. Lukeaksesi pelin säännöt, kirjoita 'säännöt'.")
aloita = input("Kirjoita 'lopeta' päättääksesi ohjelman. ")

def säännöt():
    print("Never have I ever pelissä...")
    global jatka
    jatka = input("Haluaisitko pelata? kirjoita 'aloita' tai 'lopeta'. ")
    if jatka == "aloita":
        pelaa()
    if jatka == "lopeta":
        loppu()
    
def pelaa():
    valinta = random.choice(kysymys)
    print("never have I ever " + valinta)
    uusi = input("uudestaan? y, n? ")
    if uusi == "y":
        pelaa()
    elif uusi == "n":
        loppu()

def loppu():
    print("Kiitos ja näkemiin!")

if aloita == "aloita":
    pelaa()
elif aloita == "säännöt":
    säännöt()
elif aloita == "lopeta":
    loppu()
#looppi
#valinta = random.choice(kysymys)
#print("never have I ever " +  valinta)