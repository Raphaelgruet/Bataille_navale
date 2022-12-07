from Joueur import Joueur
from Outils import cls, posXY
from Mer import Mer
from colorama import Fore, Style, Back
from Coordonnee import Coordonnee
from SousMarin import SousMarin
from Direction import Direction


# Class Partie
class Partie:

	__joueurs = [None, None]
	__temps = 0
	dimensionsMers = Coordonnee(10, 5, 3)

	def __init__(self):
		Partie.lancementPartie(self)

	# partie.test(self)

	def demandeEmplacement(self, j):
		x, y, z = -1, -1, -1
		direction = None
		print("Entrez l'emplacement de votre sous-marin " + str(j + 1) + " :")
		while not 0 < x < Partie.dimensionsMers.getX()+1:
			try:
				x = int(input("  La COLONNE du debut de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < y < Partie.dimensionsMers.getY()+1:
			try:
				y = int(input("  La LIGNE du debut de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < z < Partie.dimensionsMers.getZ()+1:
			try:
				z = int(input("  La PROFONDEUR de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not (
				direction == Direction.DROITE or direction == Direction.GAUCHE or direction == Direction.HAUT or direction == Direction.BAS):
			try:
				direction = input("  La DIRECTION de votre sous-marin (\"D\"=DROITE, \"G\"=GAUCHE, \"H\"=HAUT, \"B\"=BAS) = ")
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

		# Creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur(input("Le joueur " + str(i + 1) + " entre son prénom :"))  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre", self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls()

		# choix couleur
		self.__joueurs[0].choixCouleur()
		if self.__joueurs[0].getCouleur() == Back.BLUE:
			self.__joueurs[1].setCouleur(Back.RED)
		else:
			self.__joueurs[1].setCouleur(Back.BLUE)
		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "   ", Style.RESET_ALL, ",",
			  self.__joueurs[1],
			  "aura donc la couleur", self.__joueurs[1].getCouleur() + "   ", Style.RESET_ALL)
		input()
		cls()

		# Placement des sous-marins
		for i in range(2):
			# Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			'''self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))'''

			# Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				Mer.affichagePlateauVide(1, 2, Back.GREEN)
				for o in range(len(self.__joueurs[i].getMer().getSousMarins())):
					for g in self.__joueurs[i].getMer().getSousMarins()[o].getCoords().keys():
						x, y = g.emplacementCoordonnee()
						Mer.affichagePion(x, y, self.__joueurs[i].getCouleur())
				posXY(1, 24)

				# Placement des sous-marins
				print(self.__joueurs[i].getCouleur(), self.__joueurs[i], "place ses sous-marins", Style.RESET_ALL)
				placer = False
				while not placer:
					try:
						direction, x, y, z = Partie.demandeEmplacement(self, j)
						coord = Coordonnee(x, y, z)
						self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
						placer = True
					except Exception as e:
						print(e)

				if j == len(self.__joueurs[i].getMer().getSousMarins()) - 1:
					for o in range(len(self.__joueurs[i].getMer().getSousMarins())):
						for g in self.__joueurs[i].getMer().getSousMarins()[o].getCoords().keys():
							x, y = g.emplacementCoordonnee()
							Mer.affichagePion(x, y, self.__joueurs[i].getCouleur())
				cls()
			input()

		# TODO bug de superposition des mers au niveau de l'affichage

		cls()
		posXY(1, 1)
		print("La partie peut ")
		print("C'est à " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()

		# Commencement de la partie
		while True:
			for i in range(2):

				#Affichage
				if self.__joueurs[i].getCouleur() == "B":
					couleur = Back.RED
				else:
					couleur = Back.BLUE
				Mer.affichagePlateauVide(1, 2, couleur)
				for g in self.__joueurs[i].getMer().getImpacts():  # la veux les differents positions du sous marin
					x, y = g.emplacementCoordonnee()  # la je les transforme en position pour le terminale cdm
					self.__joueurs[i].getMer().affichagePion(x, y, couleur)  # et la je les affiche
				posXY(1, 24)

				#Detection coordonnées + impact
				direction, x, y, z = Partie.demandeEmplacement(self, j)
				coord = Coordonnee(x, y, z)
				self.__joueurs[i].getMer().impact(coord)
				input()
				cls()

				# Détection victoire
				gagnant = self.testVictoire()
				if gagnant is None:
					input()
					cls()
				else:
					print("#####################################\n")
					print("  VICTOIRE de " + str(gagnant) + " !\n")
					print("#####################################")
					return True

		# Commencement partie
		# Mer.affichagePlateauVide(1, 2,couleur)
		# for g in self.__joueurs[i].getMer().getImpacts():# la veux les differents positions du sous marin
		# 	x,y=g.emplacementCoordonnee() #la je les transforme en position pour le terminale cdm
		# 	self.__joueurs[i].getMer().affichagePion(x, y, couleur) # et la je les affiche
		# posXY(1, 24)
		# direction, x, y, z = Partie.demandeEmplacement(self,j)
		# coord = Coordonnee(x, y, z)
		# self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
		# input()
		# cls()
#
	# affichage merJ2Vide et demande au j1 des coordonnees pour impact
	# verification du win et affichage resultat
	# passage au j2 avec la merVide du j1 et demande des coordonnees pour impact
	# affichage resultat
	# boucle
	# affichage merJ2 et demande au j1 des coordonnees pour impact
	# verification du win et affichage resultat
	# passage au j2 avec la mer du j1 et demande des coordonnees pour impact
	# affichage resultat

	def testVictoire(self):
		# Fonction qui retourne le joueur qui a gagné la partie dans le cas ou celle-ci est terminée,
		# dans le cas contraire la fonction retourne None
		for i in range(2):
			if self.__joueurs[i].getPV() == 0:
				return self.__joueurs[i]
		return None

	def test(self):
		cls()
		Mer.affichagePlateauVide(1, 2, Back.GREEN)
		posXY(1, 24)
		print("boujour, vous voici sur le jeu de bateille navale ")
		input("appuyer sur entrer pour commencer la partie")
		cls()

		# Creation des joueurs

		self.__joueurs[1] = Joueur("b")
		self.__joueurs[0] = Joueur("c")  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre",
			  self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls()

		# choix couleur

		self.__joueurs[0].setCouleur(Back.RED)
		self.__joueurs[1].setCouleur(Back.BLUE)
		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "   ", Style.RESET_ALL, ",",
			  self.__joueurs[1],
			  "aura donc la couleur", self.__joueurs[1].getCouleur() + "   ", Style.RESET_ALL)
		input()
		cls()

		# Placement des sous-marins
		for i in range(2):
			# Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))

			# Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				Mer.affichagePlateauVide(1, 2, Back.GREEN)
				for o in range(len(self.__joueurs[i].getMer().getSousMarins())):
					for g in self.__joueurs[i].getMer().getSousMarins()[o].getCoords().keys():
						x, y = g.emplacementCoordonnee()
						Mer.affichagePion(x, y, self.__joueurs[i].getCouleur())
				# Placement des sous-marins
				posXY(1, 24)
				self.__joueurs[i].getMer().getSousMarins()[j].placer(Coordonnee(1, j + 1, 1), Direction.DROITE)
				input()

				if j == len(self.__joueurs[i].getMer().getSousMarins()) - 1:
					for o in range(len(self.__joueurs[i].getMer().getSousMarins())):
						for g in self.__joueurs[i].getMer().getSousMarins()[o].getCoords().keys():
							x, y = g.emplacementCoordonnee()
							Mer.affichagePion(x, y, self.__joueurs[i].getCouleur())
				cls()

		# TODO bug de superposition des mers au niveau de l'affichage

		cls()
		posXY(1, 1)
		print("La partie peut ")
		print("C'est à " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()

	# def saugerde(self...):
	# def savegarde(self...)