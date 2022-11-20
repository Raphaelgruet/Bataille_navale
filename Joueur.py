from Mer import Mer
from colorama import Fore, Style, Back
from Outils import cls
class joueur:

	__mer = Mer()
	__nom = ""
	__couleur=""
	def __init__(self, nom):
		self.__nom = nom

	def __str__(self):
		return str(self.__nom)

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
	def choixCouleur(self):  # permet de savoir quelles couleur va choisir le premier joueur
		couleurChoisi = False
		while (couleurChoisi == False):
			try:
				print(Fore.GREEN, "quelle couleur voulez vous en tant que ", self.getNom(),", faites le choix entre, ""R"" pour rouge ou ""B"" pour bleu ?")
				print(Fore.RED, "")
				self.setCouleur(input(" "))
				if (self.getCouleur() == "B" or self.getCouleur() == "R"):
					print(Style.RESET_ALL)
					couleurChoisi = True
					cls()
			except ValueError:
				pass

