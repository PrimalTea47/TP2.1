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
	if p != []:
		depiler(p)
		return depiler(p)

print(avant_dernier([1]))