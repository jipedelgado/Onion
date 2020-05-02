
import sys
import numpy as np

''' Recherche du point de plus grande abscisse
'''
def PointPlusGrandeAbscisse(listeDePoints):
	pointMax = [-sys.maxsize,0]
	for point in listeDePoints:
		if point[0] > pointMax[0]:
			pointMax = point[:]
	return pointMax

def ComplexePlusGrandeAbscisse(listeDeComplexes):
	# retourne le complexe de plus grande partie réeele et de plus petite partie imaginaire
 
	complexeMax = complex(-sys.maxsize,0)
	listeAbscisseMax = []
	realMax = complexeMax.real

	for complexe in listeDeComplexes:
		if complexe.real > realMax:
			realMax = complexe.real

	for complexe in listeDeComplexes:
		if complexe.real == realMax:
			listeAbscisseMax.append(complexe)

	imagMini = sys.maxsize
	complexeMinImag = complex(0)
	for complexe in listeAbscisseMax:
		if complexe.imag < imagMini:
			imagMini = complexe.imag
			complexeMinImag = complexe

	return complexeMinImag

def GetAngle(complex1, complex2):
	if complex1 == 0 or complex2 == 0 or complex1 == complex2:
		return sys.maxsize
	else:
		angle = np.angle(complex1, deg  =True)-np.angle(complex2, deg=True)
		angle  =angle % 360
		return angle

def PointToComplex(point):
	return complex(point[0], point[1])

def ListePointToListComplex(listePoints):
	listeComplexe = []
	for point in listePoints:
		listeComplexe.append(PointToComplex(point))
	return listeComplexe

def ListeAnglesSuccessifs(listeComplexe):
	liste = []
	for i in range(0,len(listeComplexe)-1):
		liste.append(GetAngle(listeComplexe[i+1],listeComplexe[i]))
	return liste

def ListeAnglesSuccessifsFromOrigine(listeComplexe, origine):
	liste = []
	for element in listeComplexe:
		liste.append(GetAngle(element,origine))
		print('angle =',GetAngle(element,origine))
	return liste

def GetEnveloppeConvexe(listeComplexes):
	# initialisations
	angleMin = sys.maxsize
	Enveloppe  =[]
	ListePoints = listeComplexes[:]
	vecteurCourant = complex(0)

	# le premier de l'enveloppe est le point de plus grande abscisse ( partie réelle)
	# et de plus petite ordonnée
	premier = ComplexePlusGrandeAbscisse(listeComplexes)
	Enveloppe.append(premier)

	# on est sûr que tous les points sont à gauche de la droite (x=j)
	PointOrigine = premier
	vecteurOrigine = complex(0,1)
	pointMini = premier

	while len(ListePoints) > 0:

		# recherche de l'angle mini
		angleMin = sys.maxsize
		for pointCourant in ListePoints:
			vecteurCourant = pointCourant-PointOrigine
			angle = GetAngle(vecteurCourant, vecteurOrigine)
			if angle <= angleMin:
				angleMin = angle

		# recherche des points dont l'argument est égal à l'angle mini
		listePointsMini = []
		for pointCourant in ListePoints:
			vecteurCourant = pointCourant-PointOrigine
			angle = GetAngle(vecteurCourant, vecteurOrigine)
			if angle == angleMin:
				listePointsMini.append(pointCourant)

		# Recherche du point de listePointsMini le plus proche de PointOrigine
		distanceMini = sys.maxsize
		for pointCourant in listePointsMini:
			distance = abs(pointCourant-PointOrigine)
			if distance <= distanceMini:
				distanceMini = distance
				pointMini = pointCourant

		# traitement
		if pointMini == premier:
			return Enveloppe
		else:
			Enveloppe.append(pointMini)
			ListePoints.remove(pointMini)
			vecteurOrigine = pointMini-PointOrigine
			PointOrigine = pointMini
	

def Diff(liste1, liste2):
	listeDiff = []
	for element in liste1:
		if not element in liste2:
			listeDiff.append(element)
	return listeDiff