import Mer
from Joueur import Joueur
from Outils import cls, posXY
from Mer import Mer
from colorama import Fore, Style, Back
from Coordonnee import Coordonnee
from SousMarin import SousMarin
from Direction import Direction


class partie:
	__joueurs = [None, None]
	__temps = 0

	def __init__(self):
		self.lancementPartie()

	# partie.test(self)

	def demandeEmplacement(self, j):
		x, y, z = -1, -1, -1
		direction = None
		while not 0 < x < 11:  # Valeur "hardcoded" à changer avec la taille de la mer
			try:
				x = int(input("Entrez la ligne du debut de votre sousMarin " + str(j + 1) + "\n"))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < y < 6:
			try:
				y = int(input("Entrez la colone du debut de votre sousMarin " + str(j + 1) + "\n"))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < z < 4:
			try:
				z = int(input("Entrez la profondeur du debut de votre sousMarin " + str(j + 1) + "\n"))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not (
				direction == Direction.DROITE or direction == Direction.GAUCHE or direction == Direction.HAUT or direction == Direction.BAS):  # FAIT : Correction de la condition
			try:
				direction = input("Entrez la direction de votre sousMarin " + str(
					j + 1) + " (\"D\"=DROITE, \"G\"=GAUCHE, \"H\"=HAUT, \"B\"=BAS)\n")
				if direction == "D":
					direction = Direction.DROITE
				elif direction == "B":
					direction = Direction.BAS
				elif direction == "H":
					direction = Direction.HAUT
				else:
					direction = Direction.GAUCHE
			except:
				print("vous avez fait une erreur, veillez recommencer")
		return direction, x, y, z

	def lancementPartie(self):

		cls()
		Mer.affichagePlateauVide(1, 2, Back.GREEN)
		posXY(1, 24)
		print("boujour, vous voici sur le jeu de bateille navale ")
		input("appuyer sur entrer pour commencer la partie")
		cls()

		# creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur(input("Le joueur " + str(
				i + 1) + " entre son prénom :"))  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre",
			  self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls()
		# choix couleur
		self.__joueurs[0].choixCouleur()
		if self.__joueurs[0].getCouleur() == "B":
			self.__joueurs[1].setCouleur("R")
		else:
			self.__joueurs[1].setCouleur("B")
		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + ",", self.__joueurs[1],
			  "aura donc la couleur", self.__joueurs[1].getCouleur())
		input()
		cls()

		# placement des sous-marins
		for i in range(2):
			if self.__joueurs[i].getCouleur() == "B":
				couleur = Back.BLUE
			else:
				couleur = Back.RED
			# Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			'''self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))'''
			# Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				Mer.affichagePlateauVide(1, 2, Back.GREEN)
				if j != 0:
					for g in self.__joueurs[i].getMer().getSousMarins()[j].getCoords().keys():
						x, y = g.emplacementCoordonnee()
						Mer.affichagePion(x, y, couleur)
				posXY(1, 24)

				# Placement des sous-marins
				print(couleur, self.__joueurs[i], "place ses sous-marins", Style.RESET_ALL)
				direction, x, y, z = partie.demandeEmplacement(self, j)
				coord = Coordonnee(x, y, z)
				self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
				if j == len(self.__joueurs[i].getMer().getSousMarins()) - 1:
					for g in self.__joueurs[i].getMer().getSousMarins()[j].getCoords().keys():
						x, y = g.emplacementCoordonnee()
						Mer.affichagePion(x, y, couleur)
				cls()
		cls()
		posXY(1, 1)
		print("La partie commence !")
		print("Au joueur " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()

		# commencemment partie
		while True:
			for i in range(2):

				#Affichage
				if self.__joueurs[i].getCouleur() == "B":
					couleur = Back.RED
					couleur1 = Back.RED
				else:
					couleur = Back.BLUE
					couleur1 = Back.RED
				Mer.affichagePlateauVide(1, 2, couleur)
				for g in self.__joueurs[i].getMer().getImpacts():  # la veux les differents positions du sous marin
					x, y = g.emplacementCoordonnee()  # la je les transforme en position pour le terminale cdm
					self.__joueurs[i].getMer().affichagePion(x, y, couleur)  # et la je les affiche
				posXY(1, 24)

				#Detection coordonnées + impact
				direction, x, y, z = partie.demandeEmplacement(self, j)
				coord = Coordonnee(x, y, z)
				self.__joueurs[i].getMer().impact(coord)

				#Détection victoire
				gagnant = self.testVictoire()
				if gagnant is None:
					input()
					cls()
				else:
					print("#####################################\n")
					print("  VICTOIRE de " + str(gagnant) + " !\n")
					print("#####################################")
					return True

	def testVictoire(self):
		# Fonction qui retourne le joueur qui a gagné la partie dans le cas ou celle-ci est terminée,
		# dans le cas contraire la fonction retourne None
		for i in range(2):
			if self.__joueurs[i].getPV() == 0:
				return self.__joueurs[i]
		return None

	def test(self):
		for i in range(2):
			self.__joueurs[i] = Joueur("b")  # Creation des joueurs à partir du nom entré dans le terminal
		self.__joueurs[0].setCouleur("B")
		if self.__joueurs[0].getCouleur() == "B":
			self.__joueurs[1].setCouleur("R")
		else:
			self.__joueurs[1].setCouleur("B")
		# placement des sous-marins
		for i in range(2):
			# Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			# Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				if self.__joueurs[i].getCouleur() == "B":
					couleur = Back.BLUE
				else:
					couleur = Back.RED
				cls()
				Mer.affichagePlateauVide(1, 2, Back.GREEN)
				# Placement des sous-marins
				if j != 0:
					for g in self.__joueurs[i].getMer().getSousMarins()[j].getCoords().keys():
						x, y = g.emplacementCoordonnee()
						Mer.affichagePion(x, y, couleur)
				posXY(1, 24)
				print(couleur, self.__joueurs[i], "place ses sous-marins", Style.RESET_ALL)
				if i == 1:
					self.__joueurs[i].getMer().getSousMarins()[j].placer(Coordonnee(1, 1, 1), Direction.DROITE)
				else:
					self.__joueurs[i].getMer().getSousMarins()[j].placer(Coordonnee(1, 2, 1), Direction.DROITE)
				if j == len(self.__joueurs[i].getMer().getSousMarins()) - 1:
					for g in self.__joueurs[i].getMer().getSousMarins()[j].getCoords().keys():
						x, y = g.emplacementCoordonnee()
						Mer.affichagePion(x, y, couleur)
				input()
				cls()

		posXY(1, 1)
		print("nous pouvons commencer")
		print("au joueur " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()

# def saugerde(self...):
# def savegarde(self...)
