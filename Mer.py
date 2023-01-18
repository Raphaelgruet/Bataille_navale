from colorama import Fore, Style, Back
from Outils import posXY, cls
from Coordonnee import Coordonnee

# Class de Mer
class Mer:

	__sousMarins = []
	__impacts = []
	__impactsType = {}
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
		self.__impactsType = {}


	def affichage(self, couleurPlateau, couleurPion, modeAffichage):
		cls()
		Mer.affichagePlateauVide(1, 2, couleurPlateau)
		if modeAffichage:
			for o in range(len(self.__sousMarins)):
				for i in self.__sousMarins[o].getCoords().keys():
					x, y = i.emplacementCoordonnee()
					Mer.affichagePion(x, y, couleurPion)
		else:
			Mer.affichageImpact(self, 0, modeAffichage)
		Mer.legende(self)
		posXY(1, 24)

	def affichageEnSolo(self, couleurPlateau, modeAffichage):
		if modeAffichage:
			Mer.affichagePlateauVide(1, 2, couleurPlateau)
			for o in range(len(self.__sousMarins)):
				for i in self.__sousMarins[o].getCoords().keys():
					x, y = i.emplacementCoordonnee()
					Mer.affichagePion(x, y, Back.WHITE)
			couleur = None
			valeurEmplacement = None
			Mer.affichageImpact(self,0, modeAffichage)
		else:
			Mer.affichagePlateauVide(1, 22, couleurPlateau)
			Mer.affichageImpact(self, 20, modeAffichage)
		Mer.legende(self)
		posXY(1, 42)

	def affichageImpact(self, posY, modeAffichage):
		couleur = None
		valeurEmplacement = None
		if self.__impactsType=={} or modeAffichage == True :
			for impact in self.__impacts:
				x, y = impact.emplacementCoordonnee()
				couleur = Back.BLUE
				Mer.affichagePion(x, y + posY, couleur)
			for o in range(len(self.__sousMarins)):
				for i in self.__sousMarins[o].getCoords().keys():
					couleur = self.couleurImpact(self.__sousMarins[o].getCoords()[i], modeAffichage)
					x, y = i.emplacementCoordonnee()
					Mer.affichagePion(x, y+posY, couleur)
		else:
			for key in self.__impactsType.keys():
				couleur = self.couleurImpact(self.__impactsType[key], modeAffichage)
				x, y = key.emplacementCoordonnee()
				Mer.affichagePion(x, y + posY, couleur)

	def couleurImpact(self, valeurEmplacement, modeAffichage):
		if valeurEmplacement == "o":
			if not modeAffichage:
				return Back.BLACK
			else:
				return Back.WHITE
		elif valeurEmplacement == "v":
			return Back.CYAN
		elif valeurEmplacement == "t":
			return Back.RED
		elif valeurEmplacement == "r":
			return Back.WHITE
		else:
			return Back.LIGHTRED_EX

	def legende(self):
		posXY(180, 6)
		print(Back.BLUE, "  ", Style.RESET_ALL, " veut dire que rien n'a ")
		posXY(180, 7)
		print("      ete touche ")
		posXY(180, 8)
		print(Back.CYAN, "  ", Style.RESET_ALL, " annonce la vue d'un ")
		posXY(180, 9)
		print("      sous marin")
		posXY(180, 10)
		print(Back.RED, "  ", Style.RESET_ALL, " annonce que le sous marin")
		posXY(180, 11)
		print("      est touche")
		posXY(180, 12)
		print(Back.LIGHTRED_EX, "  ", Style.RESET_ALL, " annonce que le sous marin" )
		posXY(180, 13)
		print("      est coule")

	def ajouterSousMarin(self, sousmarin):
		self.__sousMarins.append(sousmarin)
		sousmarin.setMer(self)

	def affichagePion(x, y, couleur):
		print(couleur)
		posXY(x, y)
		print("   ")
		posXY(x, y + 1)  # a tester
		print("   ")
		print(Style.RESET_ALL)

	def affichageCaseVide(x, y):
		hCase = 3
		lCase = 5
		for j in range(hCase):
			posXY(x, j + y)
			print("  ")
		for j in range(lCase):
			posXY(j + x, y)
			print(" ")
		for j in range(hCase):
			posXY(x + lCase, j + y)
			print("  ")
		for j in range(lCase):
			posXY(j + x, y + hCase)
			print("   ")

	def affichagePlateauVide(x, y, couleur):
		hCase = 3
		lCase = 5

		for k in range(3):
			posXY(7 + k * 60, y)
			print("profondeur:", k * 100 + 100)
			posXY(6 + k * 60, y + 2)
			print("   1    2    3    4    5    6    7    8    9    10  ")
			for i in range(1, 6):
				posXY(4 + k * 60, y + 2 + i * 3)
				print(i)
			print(couleur)
			for i in range(5):
				for j in range(10):
					Mer.affichageCaseVide(k * 60 + x + lCase * (j + 1), (y + hCase * (i + 1)))
			print(Style.RESET_ALL)
			posXY(1, 24)

	def impact(self, coordonneImpact):
		# Fonction qui ajoute les impacts dans la liste d'impacts et change l'état des coordonnées des sous-marins
		# en fonction la position de l'impact.

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
								#print("TOUCHÉ !")
						if sousMarin.getCoords()[coord] == 't':
							nbrTouche += 1
					if nbrTouche == sousMarin.getTaille():
						#print("COULÉ !")
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
									#print("SOUS-MARIN EN VU !")
									#input()
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
	def addImpact(self, coordonnee):
		return self.__impacts.append(coordonnee)
	def getImpactsType(self):
		return self.__impactsType
	def setImpactsType(self, keys, value):
		self.__impactsType[keys]=value
