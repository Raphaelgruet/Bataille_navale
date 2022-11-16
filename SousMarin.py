from Coordonnee import Coordonnee
from Direction import Direction


class SousMarin:

	__taille = 0
	__coords = {}
	__mer = None

	def __init__(self, taille):
		self.__taille = taille

	def placer(self, coordonnee, direction):

		if coordonnee.getZ() < 1 or coordonnee.getZ() > 3:
			raise Exception("Le sous marin n'est pas a la bonne hauteur")

		if direction == Direction.HAUT:
			if coordonnee.getY() - self.__taille > 0:
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX(), coordonnee.getY() -i, coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")
		if direction == Direction.DROITE:
			if coordonnee.getX() + self.__taille <= self.__mer.getDimentionX():
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX()+i, coordonnee.getY(), coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")
		if direction == Direction.BAS:
			if coordonnee.getY() + self.__taille <= self.__mer.getDimentionY():
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX(), coordonnee.getY() +i, coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")
		if direction == Direction.GAUCHE:
			if coordonnee.getX() - self.__taille > 0:
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX()-i, coordonnee.getY(), coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")

	'''def toucher(self, coordonnee):
		if coordonnee in self.__coord.keys():
			if self.__coord =='''

	def getTaille(self):
		return self.__taille

	def getCoords(self):
		return self.__coords

	def getMer(self):
		return self.__mer

	def setMer(self, mer):
		self.__mer = mer
