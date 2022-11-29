from Coordonnee import Coordonnee
from Direction import Direction
from Mer import Mer

class SousMarin:
	__taille = 0
	__coords = {}
	__mer = None

	def __init__(self, taille):
		self.__taille = taille

	def __str__(self):
		toString = "["
		for i in range(self.__taille):
			toString += list(self.__coords.keys())[i].__str__()
			if i < self.__taille - 1:
				toString += ", "
		toString += "]"
		return toString

	def placer(self, coordonnee, direction):

		if coordonnee.getZ() < 1 or coordonnee.getZ() > 3:
			raise Exception("La profondeur du sous marin est incorrect")

		if direction == Direction.HAUT:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (smCoord.getX() == coordonnee.getX() and
							coordonnee.getY() - self.__taille < smCoord.getY() <= coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getY() - self.__taille > 0:
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX(), coordonnee.getY() - i, coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")
		if direction == Direction.DROITE:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (coordonnee.getX() + self.__taille > smCoord.getX() >= coordonnee.getX() and
							smCoord.getY() == coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getX() + self.__taille <= self.__mer.getDimentionX():
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX() + i, coordonnee.getY(), coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")
		if direction == Direction.BAS:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (smCoord.getX() == coordonnee.getX() and
							coordonnee.getY() + self.__taille > smCoord.getY() >= coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getY() + self.__taille <= self.__mer.getDimentionY():
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX(), coordonnee.getY() + i, coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")
		if direction == Direction.GAUCHE:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (coordonnee.getX() - self.__taille < smCoord.getX() <= coordonnee.getX() and
							smCoord.getY() == coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getX() - self.__taille > 0:
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX() - i, coordonnee.getY(), coordonnee.getZ())
					self.__coords[coord] = 'O'
			else:
				raise Exception("Le sous marin est trop grand pour etre placé ici")

	def toucher(self, coordonnee):
		if coordonnee in self.__coord.keys():
			if self.__coord[coordonnee] == 'O':
				self.__coords[coordonnee] = 'T'
		coule = True
		for etat in self.__coords.values():
			if etat != 'T':
				coule = False
		if coule:
			print("Sous marin coulé")
			for coord in self.__coords.keys():
				self.__coords[coord] = 'C'

	def getTaille(self):
		return self.__taille

	def getCoords(self):
		return self.__coords

	def getMer(self):
		return self.__mer

	def setMer(self, mer):
		self.__mer = mer
