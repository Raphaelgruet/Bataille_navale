from Coordonnee import Coordonnee
from Direction import Direction

# Class de SousMarin
class SousMarin:

	# o = non vu
	# v = vu
	# t = touché
	# c = coulé

	__taille = 0
	__coords = None
	__mer = None

	def __init__(self, taille):
		self.__taille = taille
		self.__coords = {}
		self.__mer = None

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
			if coordonnee.getY() - self.__taille+1 > 0:
				self.__coords.clear()
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX(), coordonnee.getY() - i, coordonnee.getZ())
					self.__coords[coord] = 'o'
			else:
				raise Exception("Le sous marin est trop grand pour être placé ici")
		if direction == Direction.DROITE:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (coordonnee.getX() + self.__taille > smCoord.getX() >= coordonnee.getX() and
							smCoord.getY() == coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getX() + self.__taille-1 <= self.__mer.getDimentionX():
				self.__coords.clear()
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX() + i, coordonnee.getY(), coordonnee.getZ())
					self.__coords[coord] = 'o'
			else:
				raise Exception("Le sous marin est trop grand pour être placé ici")
		if direction == Direction.BAS:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (smCoord.getX() == coordonnee.getX() and
							coordonnee.getY() + self.__taille > smCoord.getY() >= coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getY() + self.__taille-1 <= self.__mer.getDimentionY():
				self.__coords.clear()
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX(), coordonnee.getY() + i, coordonnee.getZ())
					self.__coords[coord] = 'o'
			else:
				raise Exception("Le sous marin est trop grand pour être placé ici")
		if direction == Direction.GAUCHE:
			for sousMarin in self.__mer.getSousMarins():
				for smCoord in sousMarin.getCoords():
					if (coordonnee.getX() - self.__taille < smCoord.getX() <= coordonnee.getX() and
							smCoord.getY() == coordonnee.getY() and
							smCoord.getZ() == coordonnee.getZ()):
						raise Exception("Il y a déjà un sous marin à cet emplacement")
			if coordonnee.getX() - self.__taille+1 > 0:
				self.__coords.clear()
				for i in range(self.__taille):
					coord = Coordonnee(coordonnee.getX() - i, coordonnee.getY(), coordonnee.getZ())
					self.__coords[coord] = 'o'
			else:
				raise Exception("Le sous marin est trop grand pour être placé ici")

	def toucher(self, coordonnee):
		if coordonnee in self.__coord.keys():
			if self.__coord[coordonnee] == 'o':
				self.__coords[coordonnee] = 't'
		coule = True
		for etat in self.__coords.values():
			if etat != 't':
				coule = False
		if coule:
			print("Sous marin coulé")
			for coord in self.__coords.keys():
				self.__coords[coord] = 'c'

	def getTaille(self):
		return self.__taille

	def getCoords(self):
		return self.__coords

	def getMer(self):
		return self.__mer

	def setMer(self, mer):
		self.__mer = mer
