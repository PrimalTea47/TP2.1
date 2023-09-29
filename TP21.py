def creer_pile():
	return []

def empiler(e,p):
	p.append(e)
	return p


def depiler(p):
	return p.pop()



def pile_vide(p):
	return creer_pile()

def sommet(p):
	empiler(p[-1],p)
	return depiler(p)


def taille(p):
	c=0
	while p != []:
		depiler(p)
		c+=1
	return c


#############################################################################################
'''
UNIQUEMENT UTILISER empiler() depiler() pile_vide()
'''
#############################################################################################
'''
pile = []
empiler(5,pile)
empiler(7,pile)
empiler(2,pile)
empiler(4,pile)
print(pile)

depiler(pile)
empiler(8,pile)
empiler(1,pile)
empiler(3,pile)
print(pile)
'''

'''
def pile_contient(element,pile):
	for i in reversed(pile):
		if depiler(pile) == element:
			return True	
	return False


#print(pile_contient(8,[4,8,9,5,0]))

def somme(p):
	total = 0
	for i in reversed(p):
		total += depiler(p)
	return total
# print(somme([4,8,9,5,0]))

def avant_dernier(p):
    if len(p) > 1:
		depiler(p)
		return depiler(p)

print(avant_dernier([5,9,7,8]))
'''

def defiler(f):
    del f[0]

def enfiler(x, f):
    f.append(x)
'''
def croisement(f1, f2):
    f3 = []
    while f1 and f2:
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

print(croisement([0, 1, 1, 0, 1], [0, 2, 2, 2, 0, 2, 0]))
'''
'''
def tri(f):
	even = []
	odd = []
	for i in f:
		if i % 2 == 0:
			enfiler(i,even)
		else:
			enfiler(i,odd)
	return even, odd
print(tri([2,6,5,4,8,7,3,1,8,89,4,87,78]))
'''

from collections import deque
from random import randint

file_attente=['1','2','3','4','5','6','7','8','9','10']
d = deque(file_attente)

def caisse(f):
	temps = []
	for i in range(5):
		temps.append(randint(3,10))
	
	while d:
		if 0 in temps:
			