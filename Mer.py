from colorama import Fore, Style, Back
from Outils import posXY, cls

# Class de Mer
class Mer:

	__sousMarins = []
	__impacts = []
	__dimentionX = 10
	__dimentionY = 5
	__dimentionZ = 3
	'''__dimentionX = Partie.dimensionsMers.getX()
	__dimentionY = Partie.dimensionsMers.getY()
	__dimentionZ = Partie.dimensionsMers.getZ()'''
	# TODO dimensions à partir de Partie

	def __init__(self):
		self.__sousMarins = []
		self.__impacts = []

	def ajouterSousMarin(self, sousmarin):
		self.__sousMarins.append(sousmarin)
		sousmarin.setMer(self)

	def affichageCaseVide(x, y):

		hCase = 3
		lCase = 5
		for j in range (hCase):
			posXY(x, j + y)
			print("  ")
		for j in range (lCase):
			posXY(j+x,y)
			print(" ")
		for j in range(hCase):
			posXY(x+lCase, j + y)
			print("  ")
		for j in range (lCase):
			posXY(j+x,y+hCase)
			print("   ")

	def affichagePlateauVide(x, y, couleur):
		hCase = 3
		lCase = 5

		for k in range(3):
			posXY(7 + k * 60, 1)
			print("profondeur:", k * 100+100)
			posXY(6 + k * 60, 4)
			print("   1    2    3    4    5    6    7    8    9    10  ")
			for i in range(1,6):
				posXY(4 + k * 60, 4+i*3)
				print (i)
			print(couleur)
			for i in range(5):
				for j in range(10):
					Mer.affichageCaseVide(k*60+x+lCase*(j+1),(y+hCase*(i+1)))
			print(Style.RESET_ALL)

	def impact(self, coordonneImpact):
		# Fonction qui ajoute les impacts dans la liste d'impacts et change l'état des coordonnées des sous-marins
		# en fonction la position de l'impact.
		# TODO etat de position "en vue"

		if 0 < coordonneImpact.x <= self.__dimentionX and 0 < coordonneImpact.x <= self.__dimentionY and 0 < coordonneImpact.x <= self.__dimentionZ:
			if coordonneImpact not in self.__impacts:
				self.__impacts.append(coordonneImpact)
				for sousMarin in self.__sousMarins:
					nbrTouche = 0
					for coord in sousMarin.getCoords():
						if coord == coordonneImpact:
							if sousMarin.getCoords()[coord] != 'c' and sousMarin.getCoords()[coord] != 't':
								sousMarin.getCoords()[coord] = 't'
								print("TOUCHÉ !")
						if sousMarin.getCoords()[coord] == 't':
							nbrTouche += 1
					if nbrTouche == sousMarin.getTaille():
						print("COULÉ !")
						for coord in sousMarin.getCoords():
							sousMarin.getCoords()[coord] = 'c'
				return True
		return False

	def getDimentionZ(self):
		return self.__dimentionZ
	def setDimentionZ(self, value):
		self.__dimentionZ = value
	def getDimentionX(self):
		return self.__dimentionX
	def setDimentionX(self, value):
		self.__dimentionX = value
	def getDimentionY(self):
		return self.__dimentionY
	def setDimentionY(self, value):
		self.__dimentionY = value
	def getSousMarins(self):
		return self.__sousMarins
	def getImpacts(self):
		return self.__impacts
	def affichagePion(x, y, couleur):
		print(couleur)
		posXY(x, y)
		print("   ")
		posXY(x, y + 1)  # a tester
		print("   ")
		print(Style.RESET_ALL)