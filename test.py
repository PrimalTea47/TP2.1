
def depiler(p):
    return p.pop()


def taille(p):
    c=0
    copie = p.copy()
    while copie != []:
        depiler(copie)
        c+=1
    return c
# print(taille([9,7,2,1,5,4,8,0,6]))



def avant_dernier(p : list):
    if taille(p) > 1:
        depiler(p)
        return depiler(p)
# print(avant_dernier([9,7,2,1,5,4,8,0,6]))

def somme(p):
    total = 0
    for i in reversed(p):
        total += depiler(p)
    return total
# print(somme([9,7,2,1,5,4,8,0,6]))

def pile_contient(element,pile):
    for i in reversed(pile):
        if depiler(pile) == element:
            return True 
    return False

# print(pile_contient(0,[9,7,2,1,5,4,8,0,6]))

from collections import deque

def defiler(f):
    del f[0]

def enfiler(x, f):
    f.append(x)

def croisement(f1, f2):
    f3 = []
    while f1 != [] and f2 != []:
        if f1[0] == 0 and f2[0] == 0:
            defiler(f1)
            defiler(f2)
            enfiler(0, f3)
        elif f1[0] == 0:
            enfiler(f2[0], f3)
            defiler(f1)
            defiler(f2)
        elif f2[0] == 0:
            enfiler(f1[0], f3)
            defiler(f1)
            defiler(f2)
        else:
            enfiler(f1[0], f3)
            defiler(f1)


    while f1 != []:
        enfiler(f1[0], f3)
        defiler(f1)
    while f2 != []:
        enfiler(f2[0], f3)
        defiler(f2)

    return f3

# print(croisement([0, 1, 1, 0, 1], [0, 2, 2, 2, 0, 2, 0]))

from collections import deque
from random import randint

def caisse(f : list) :
    #Initialiser la file d'attente et les temps aléatoires à chaque caisses
    d = deque(f)
    temps = [randint(3, 10) for p in range(5)]
    print(temps)
    while True:
        for temps_caisse in temps:
            if len(d) == 0:
                return d,temps
            #Si un temps à la caisse est égal à 0, enlever le premier de la file d'attente, redonner un temps aléatoire en 3 et 10 à temps écoulé
            elif temps_caisse == 0:
                d.popleft()
                temps[temps.index(temps_caisse)] = randint(3, 10)
                print(f'File d\'attente --> {d} & temps au caisse --> {temps}')
            #Sinon diminuer le temps de 1
            else:
                temps[temps.index(temps_caisse)] -= 1
file_attente = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# print(caisse(file_attente))

def operation(a,b,op):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return a-b


def calculatrice_polonaise(expression):
    pile = []
    for element in expression.split(' '):
        if element.isdigit():
            pile.append(element)
        else:
            pile.append(operation(int(pile.pop()),int(pile.pop()),element))
    return pile
print(calculatrice_polonaise('2 3 + 5 *'))