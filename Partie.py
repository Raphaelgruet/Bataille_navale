from Joueur import joueur
from Outils import cls, posXY
from Mer import Mer
from colorama import Fore, Style, Back
from Coordonnee import Coordonnee
from SousMarin import SousMarin
from Direction import Direction
class partie:

	__joueur1 = None
	__joueur2 = None
	__temps = 0

	def __init__ (self):
		partie.lancementPartie(self)

	def lancementPartie(self):
		cls()
		print(Back.GREEN)
		Mer.affichagePlateauVide(1, 2)
		print(Style.RESET_ALL)
		posXY(1,24)
		print("boujour, vous voici sur le jeu de bateille navale ")
		#input("appuyer sur entrer pour commencer la partie")
		cls()
		#creation des joueur
		print("que le joueur 1 entre son prenom")
		self.__joueur1=joueur("C")#test
		#self.__joueur1 = joueur(input())
		print("que le joueur 2 entre son prenom")
		#self.__joueur2=joueur(input())
		self.__joueur2 = joueur("A")#test
		print("cette bataille opposera ", self.__joueur1.getNom().upper(), " contre ",self.__joueur2.getNom().upper())
		print("bonne bataille")
		#input()
		cls()
		#savoir la couleur
		#self.__joueur1.choixCouleur()
		self.__joueur1.setCouleur("B")#test
		if self.__joueur1.getCouleur()=="B":
			self.__joueur2.setCouleur("R")
		else:
			self.__joueur2.setCouleur("B")

		#placement des sousmarin J1
		print ("c est a", self.__joueur1.getNom()," de placer ces sousmarin")
		sousMarin1 = SousMarin(4)
		self.__joueur1.getMer().ajouterSousMarin(sousMarin1)
		"""X = int(input("entrez la ligne du debut de votre sousMarin\n"))
		Y = int(input("entrez la colone du debut de votre sousMarin\n"))
		Z = int(input("entrez la profondeur du debut de votre sousMarin\n"))
		c=Coordonnee(X, Y, Z)"""
		c = Coordonnee(1, 1, 1)#test
		sousMarin1.setMer(self.__joueur1.getMer())
		#direction=  il faut m'aider a écrire cela
		sousMarin1.placer(c, Direction.DROITE)
		cls()
		print(Back.GREEN)
		Mer.affichagePlateauVide(1, 2)
		print(Style.RESET_ALL)

		if self.__joueur1.getcouleur()=="B":
			couleur=Back.BLUE
		for i in sousMarin.getCoords().keys():
			x,y=i.emplacementCoordonnee()
			affichagePion(x, y, couleur)
		#placement des sousmarin
			# affichage merJ1
			# demande de placement de un sous marin
			# affichage merJ1
			# demande de placement de un sous marin
			# affichage merJ1
			# demande de placement de un sous marin
			# affichage merJ1
			# effacage de la merJ1 et prevention du changement de mer
			# affichage merJ2
			# demande de placement de un sous marin
			# affichage merJ2
			# demande de placement de un sous marin
			# affichage merJ2
			# demande de placement de un sous marin
			# affichage merJ2
			# effacage de la merJ2 et prevention du commencement

# affichage merJ2Vide et demande au j1 des coordonnees pour impact
# verification du win et affichage resultat
# passage au j2 avec la merVide du j1 et demande des coordonnees pour impact
# affichage resultat
# boucle
# affichage merJ2 et demande au j1 des coordonnees pour impact
# verification du win et affichage resultat
# passage au j2 avec la mer du j1 et demande des coordonnees pour impact
# affichage resultat

def test():
	# affichage d'une coordonne sur plateau
	c = Coordonnee(9, 1, 1)
	print(Style.RESET_ALL)
	print(Back.RED)
	x, y = c.emplacementCoordonnee()
	posXY(x, y)
	print("   ")
	posXY(x, y + 1)  # a tester
	print("   ")
	print(Style.RESET_ALL)
	input()
	#def saugerde(self...):
	#def savegarde(self...)