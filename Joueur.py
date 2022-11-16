from Mer import Mer

class joueur:

	__mer = Mer()
	__nom = ""

	def __init__(self, nom):
		self.__nom = nom

	def __str__(self):
		return str(self.__nom)

	def setNom(self, value):
		self.__nom = value

	def getNom(self):
		return self.__nom

	def getMer(self, value):
		self.__mer = value