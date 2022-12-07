from Mer import Mer
from colorama import Fore, Style, Back
from Outils import cls

# Class Joueur
class Joueur:
	__mer = None
	__nom = ""
	__couleur = None

	def __init__(self, nom):
		self.__nom = nom
		self.__couleur = None
		self.__mer = Mer()

	def __str__(self):
		return str(self.__nom)

	def getPV(self):
		# Fonction qui retourne le nombre de pv du joueur (nombre de coordonnées de sous-marins non touchées)

		pv = 0
		for sousMarin in self.__mer.getSousMarins():
			for coord in sousMarin.getCoords().keys():
				if sousMarin.getCoords()[coord] != 't' and sousMarin.getCoords()[coord] != 'c':
					pv += 1
		return pv

	def setNom(self, value):
		self.__nom = value

	def getNom(self):
		return self.__nom

	def setCouleur(self, value):
		self.__couleur = value

	def getCouleur(self):
		return self.__couleur

	def getMer(self):
		return self.__mer

	def choixCouleur(self):  # permet de savoir quelle couleur va choisir le premier joueur
		couleurChoisi = False
		while not couleurChoisi:
			print(Fore.GREEN)
			couleur = input(self.getNom() + " choisi sa couleur entre, \"R\" pour rouge ou \"B\" pour bleu ?").upper()
			if couleur == "B":
				self.__couleur = Back.BLUE
				print(Style.RESET_ALL)
				couleurChoisi = True
			if couleur == "R":
				self.__couleur = Back.RED
				print(Style.RESET_ALL)
				couleurChoisi = True
				cls()