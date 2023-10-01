from collections import deque
from random import randint

def caisse(f: list):
    # Initialiser la file d'attente et les temps aléatoires à chaque caisse
    d = deque(f)
    temps = [randint(3, 10) for p in range(5)]
    print(f"DÉBUT ==> {d} & TEMPS ==> {temps}")
    while True:
        temps_copies = temps.copy()  # Copie de la liste temps
        for i in range(len(temps_copies)):
            # Si la file d'attente est vide, arrêter et renvoyer la file d'attente vide et les différents temps aux caisses
            if len(d) == 0:
                return d, temps
            # Si un temps à la caisse est égal à 0, enlever le premier de la file d'attente, redonner un temps aléatoire en 3 et 10 à la caisse
            elif temps_copies[i] == 0:
                d.popleft()
                temps[i] = randint(3, 10)
                print(f'File d\'attente --> {d} & temps au caisse --> {temps}')
            # Sinon diminuer le temps de la caisse i de 1
            else:
                temps[i] -= 1

file_attente = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(caisse(file_attente))
