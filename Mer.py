from colorama import Fore, Style, Back
from Outils import posXY, cls
from colorama import init
class Mer:
	__sousMarin = []
	__impact = []
	__dimentionX = 10
	__dimentionY = 5
	__dimentionZ = 3

	def ajouterSousMarin(self, sousmarin):
		self.__sousMarin.append(sousmarin)
		sousmarin.setMer(self)
	def caseVide(x, y):
		hCase = 3
		lCase = 5
		for j in range (hCase):
			posXY(x, j + y)
			print(Back.GREEN, " ", Style.RESET_ALL)
		for j in range (lCase):
			posXY(j+x,y)
			print(Back.GREEN, "  ", Style.RESET_ALL)
		for j in range(hCase):
			posXY(x+lCase, j + y)
			print(Back.GREEN, " ", Style.RESET_ALL)
		for j in range (lCase):
			posXY(j+x,y+hCase)
			print(Back.GREEN, "  ", Style.RESET_ALL)

	def plateauVide(x, y):

	def impact(self, coordonneImpact):
		if 0 < coordonneImpact.x <= self.__dimentionX and 0 < coordonneImpact.x <= self.__dimentionY and 0 < coordonneImpact.x <= self.__dimentionZ:
			if coordonneImpact not in self.__impact:
				self.__impact.append(coordonneImpact)
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
		return self.__sousMarin

	def getImpacts(self):
		return self.__impact
