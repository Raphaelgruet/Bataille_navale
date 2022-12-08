from colorama import Fore, Style, Back
from Outils import posXY, cls
from Coordonnee import Coordonnee

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


	def affichage(self, couleurPlateau, couleurPion, modeAffichage):
		cls()
		Mer.affichagePlateauVide(1, 2, couleurPlateau)
		if modeAffichage:
			for o in range(len(self.__sousMarins)):
				for i in self.__sousMarins[o].getCoords().keys():
					x, y = i.emplacementCoordonnee()
					Mer.affichagePion(x, y, couleurPion)
		else:
			couleur = None
			valeurEmplacement=None
			for impact in self.__impacts:
				x, y = impact.emplacementCoordonnee()
				couleur = Back.BLUE
				Mer.affichagePion(x, y, couleur)
			for o in range(len(self.__sousMarins)):
				for i in self.__sousMarins[o].getCoords().keys():
					valeurEmplacement = self.__sousMarins[o].getCoords()[i]
					if valeurEmplacement == "o":
						couleur = Back.BLACK
					elif valeurEmplacement == "v":
						couleur = Back.CYAN
					elif valeurEmplacement == "t":
						couleur = Back.RED
					else:
						couleur = Back.MAGENTA
					x, y = i.emplacementCoordonnee()
					Mer.affichagePion(x, y, couleur)
		posXY(1, 24)
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

	def affichagePlateauVide( x, y, couleur):
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
			posXY(1, 24)

	def impact(self, coordonneImpact):
		# Fonction qui ajoute les impacts dans la liste d'impacts et change l'état des coordonnées des sous-marins
		# en fonction la position de l'impact.
		# TODO etat de position "en vue"

		if 0 < coordonneImpact.getX() <= self.__dimentionX and 0 < coordonneImpact.getY() <= self.__dimentionY and 0 < coordonneImpact.getZ() <= self.__dimentionZ:
			if coordonneImpact not in self.__impacts:
				self.__impacts.append(coordonneImpact)
				touche = False
				for sousMarin in self.__sousMarins:
					nbrTouche = 0
					for coord in sousMarin.getCoords():
						if coord == coordonneImpact:
							touche = True
							if sousMarin.getCoords()[coord] != 'c' and sousMarin.getCoords()[coord] != 't':
								sousMarin.getCoords()[coord] = 't'
								print("TOUCHÉ !")
						if sousMarin.getCoords()[coord] == 't':
							nbrTouche += 1
					if nbrTouche == sousMarin.getTaille():
						print("COULÉ !")
						for coord in sousMarin.getCoords():
							sousMarin.getCoords()[coord] = 'c'
				if not touche:
					for sousMarin in self.__sousMarins:
						for coord in sousMarin.getCoords():
							if sousMarin.getCoords()[coord] != 'c' and sousMarin.getCoords()[coord] != 't':
								if(((coord.getX() == coordonneImpact.getX() - 1 or coord.getX() == coordonneImpact.getX() + 1) and coord.getY() == coordonneImpact.getY() and coord.getZ() == coordonneImpact.getZ()) or
									(coord.getX() == coordonneImpact.getX() and (coord.getY() == coordonneImpact.getY() - 1 or coord.getY() == coordonneImpact.getY() + 1) and coord.getZ() == coordonneImpact.getZ()) or
									(coord.getX() == coordonneImpact.getX() and coord.getY() == coordonneImpact.getY() and (coord.getZ() == coordonneImpact.getZ() - 1 or coord.getZ() == coordonneImpact.getZ() + 1))):
									sousMarin.getCoords()[coord] = 'v'
									print("SOUS-MARIN EN VU !")
									input()
			return True
		return False

		# TODO bug de vu (reécriture sur une case touché ou coulé)

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