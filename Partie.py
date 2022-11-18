from Joueur import joueur
from Outils import cls, posXY
from Mer import Mer
class partie:

	__joueur1 = None
	__joueur2 = None
	__temps = 0

	def __init__ (self, nom1, nom2):
		self.__joueur1 = joueur(nom1)
		self.__joueur2 = joueur(nom2)


	def lancerPartie():
		Mer.caseVide(60, 6)
		posXY(0,0)
		print("boujour, vous voici sur le jeu de bateille navale ")
		input("appuyer sur entrer pour commencer la partie")
		cls()




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


	#def saugerde(self...):
	#def savegarde(self...)