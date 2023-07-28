import random
with open('neverever.txt', 'r') as file:
    kysymys = file.readlines()
valinta = random.choice(kysymys)
print("never have I ever " +  valinta)
