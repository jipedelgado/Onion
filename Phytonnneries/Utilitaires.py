'''  utilitaires de manipulation de fichier et de listes
'''
import decimal

def ListeFromFile(fileName, mode= 'r'):
	try:
		with open(fileName,mode) as f:
			aListe = []
			for ligne in f:
				aListe.append(ligne.strip(' \n'))
	except IOError:
		print('fichier manquant')
	else:
		return(aListe)



def String2Liste2D(chaine):
	Liste2D =[]
	for element in chaine:
		Liste2D.append(listStr2ListDecimal(element.split(" ")))
	return Liste2D

def listStr2ListInt(liste):
# transforme une liste de strings en liste de int
	return [int(x) for x in liste]

def listStr2ListDecimal(liste):
# transforme une liste de strings en liste de int
	return [decimal.Decimal(x) for x in liste]

