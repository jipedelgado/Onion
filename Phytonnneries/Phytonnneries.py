
from Utilitaires import String2Liste2D, ListeFromFile
from module1 import GetAngle
from module1 import PointPlusGrandeAbscisse, PointToComplex,ListePointToListComplex, ListeAnglesSuccessifs,ListeAnglesSuccessifsFromOrigine
from module1 import GetEnveloppeConvexe, Diff
import matplotlib.pyplot as plt
import cmath
import math
import random

def CreateRandomFile():
	# création d'une string au format <real> <espace> <réel> <CRLF>
	aString = ""
	for i in range(0,1000):
		n = random.random()
		m = random.random()
		aString = aString + str(n) +' ' + str(m) + '\n'

	# on enregistre la chaine dans un fichier temporaire
	filename = 'monfichier.txt'
	f = open(filename,'w')
	f.write(aString)
	f.close()

	# pour contrôle et debug, peut être supprimé
	g = open(filename, 'r')	
	print("Le contenu de mon fichier est : ", g.read())
	f.close()

def PrintListe(liste):
	uneListe = liste[:]
	if len(uneListe)>0:
		reel = []
		imag = []
		for complexe in liste:
			reel.append(complexe.real)
			imag.append(complexe.imag)
		# on boucle sur le premier élément de la liste
		reel.append(reel[0])
		imag.append(imag[0])
		# on affiche la liste
		plot = plt.plot(reel, imag)
	
def onion(listeComplexes):
	interieur = listeComplexes[:]
	enveloppe = GetEnveloppeConvexe(interieur)
	while len(interieur)> 0:
		enveloppe = GetEnveloppeConvexe(interieur)
		interieur = Diff(interieur,enveloppe)
		PrintListe(enveloppe)

#main() ----------------------------------------------------------------------

CreateRandomFile()
fileName = 'monfichier.txt'
unVecteur = ListeFromFile(fileName)
autreVecteur = String2Liste2D(unVecteur)
l = ListePointToListComplex(autreVecteur)

# affiche les points
abscisse = []
ordonnee = []
for point in autreVecteur:
	abscisse.append(point[0])
	ordonnee.append(point[1])
plot = plt.scatter(abscisse, ordonnee)

onion(l)
plt.show()