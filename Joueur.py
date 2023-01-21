from Mer import Mer
from colorama import Fore, Style, Back
from Outils import cls
from Coordonnee import Coordonnee
# Class Joueur
class Joueur:

	def __init__(self, nom):
		self.__nom = nom
		self.__couleur = None
		self.__couleur2 = None
		self.__mer = Mer()
		self.__sauvegardeDerniereToucheIa = Coordonnee(0,0,0)
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

	def getMaxPV(self):
		maxPV = 0
		for sousMarin in self.getMer().getSousMarins():
			maxPV += sousMarin.getTaille()
		return maxPV
	def setNom(self, value):
		self.__nom = value

	def getNom(self):
		return self.__nom

	def setCouleur(self, value):
		self.__couleur = value

	def getCouleur(self):
		return self.__couleur

	def getCouleur2(self):
		return self.__couleur2
	def setCouleur2(self, value):
		self.__couleur2=value
	def getMer(self):
		return self.__mer
	def getSauvegardeDerniereToucheIa(self):
		return self.__sauvegardeDerniereToucheIa
	def setSauvegardeDerniereToucheIa(self,coordonne):
		self.__sauvegardeDerniereToucheIa=coordonne
	def choixCouleur(self):  # permet de savoir quelle couleur va choisir le premier joueur
		couleurChoisi = False
		while not couleurChoisi:
			print(Fore.LIGHTCYAN_EX)
			print(self.getNom() + " choisi sa couleur entre, ", Fore.LIGHTGREEN_EX, "\"V\" pour vert",
				  Fore.LIGHTCYAN_EX, " ou ", Fore.LIGHTYELLOW_EX, "\"J\" pour jaune ?")
			couleur = input().upper()
			if couleur == "V":
				self.__couleur = Back.GREEN
				self.__couleur2 = Fore.LIGHTGREEN_EX
				print(Style.RESET_ALL)
				couleurChoisi = True
			if couleur == "J":
				self.__couleur = Back.YELLOW
				self.__couleur2 = Fore.LIGHTYELLOW_EX
				print(Style.RESET_ALL)
				couleurChoisi = True
				cls()
()