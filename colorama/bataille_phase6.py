from random import randrange
import fixpath
from colorama import init, Fore, Back, Style
tab = [ [0 for i in range(17)] for j in range(17)]
tabnoir = [ [0 for i in range(16)] for j in range(16)]
colonne = 'ZABCDEFGHIJKLMNO'
ligne = "[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]"
	

#############
#           #
#  PHASE 2  #
#           #
#############

#Affichage du tableau avec le quadrillage visuel
def afficherTab(tableau):
	print("","","",end="")
	for j in range(15):
		if j<14:
			print("" , "" ,colonne[j+1],"", end="")
		else:
			print("" , "" ,colonne[j+1],"")
				
	print("","","\u250C",end="")
	for a in range (15):
		print("\u2500""\u2500""\u2500", end="")
		if a < 14:
			print("\u252C", end="")
	print("\u2510")
	for i in range(15):
		if i < 9:
			print("",i+1, end="")
		else:
			print(i+1, end="")
		for j in range (15):
			print("\u2502", tableau[j][i],"", end="")
		print("\u2502",compteurLigne(tab,i))

		if i < 14:
			print("","","\u251C",end="")
			for b in range (15):
				print("\u2500""\u2500""\u2500", end="")
				if b < 14 :
					print("\u253C", end="")
			print("\u2524")
			
	print("","","\u2514",end="")
	for a in range (15):
		print("\u2500""\u2500""\u2500", end="")
		if a < 14:
			print("\u2534", end="")
	print("\u2518")
	
	print("","","", end="")	
	for j in range(15):
		print("","",compteurColonne(tab,j), "",end="")
	print("\n")
	
#Fonction qui permet le placement aléatoire des navires entourés de mer en fonction de l'orientation horizontale ou verticale et de sa taille	
def placerNavire(tab, t_bateau):
	bateau = 0
	#Boucle tant que le bateau n'est pas dessiné
	while bateau == 0: 
		o_bateau = randrange(1,3) 
		#Si l'orientation du bateau est horizontale
		if o_bateau == 1:
			#Variables qui prennent des coordonnées aléatoires dans la grille
			x = randrange(1,17-t_bateau)
			y = randrange(1,16)
		else :
			x = randrange(1,16)
			y = randrange(1, 17-t_bateau)
		if o_bateau == 1:
			a = 0
			for i in range (y-1, y+2):
				for j in range (x-1, x+t_bateau+1):
					if tab[j][i] == 0:
						a = a
					else:
						a = a+1
			if a == 0:
				for i in range (y-2, y+1):
					for j in range (x-2, x+t_bateau):
						tab[j][i] = 9
				i = y-1
				#Mise en couleur des navires en fonction de leur taille
				for j in range (x-1, x+t_bateau-1):
					if t_bateau == 1:
						tab[j][i] = Back.MAGENTA + ' ' + Back.RESET
					if t_bateau == 2:
						tab[j][i] = Back.RED + ' ' + Back.RESET
					if t_bateau == 3:
						tab[j][i] = Back.GREEN + ' ' + Back.RESET
					if t_bateau == 4:
						tab[j][i] = Back.YELLOW + ' ' + Back.RESET
					bateau = 1
		#Si l'orientation du bateau est verticale			
		if o_bateau == 2 :
			a = 0
			for i in range (y-1, y+t_bateau+1):
				for j in range (x-1, x+2):
					if tab[j][i] == 0:
						a = a
					else:
						a = a+1
			if a == 0:
				for i in range (y-2, y+t_bateau):
					for j in range (x-2, x+1):
						tab[j][i] = 9
				j = x-1
				#Mise en couleur des navires en fonction de leur taille
				for i in range (y-1, y+t_bateau-1):
					if t_bateau == 1:
						tab[j][i] = Back.MAGENTA + ' ' + Back.RESET
					if t_bateau == 2:
						tab[j][i] = Back.RED + ' ' + Back.RESET
					if t_bateau == 3:
						tab[j][i] = Back.GREEN + ' ' + Back.RESET
					if t_bateau == 4:
						tab[j][i] = Back.YELLOW + ' ' + Back.RESET
					bateau = 1
				
#Fonction qui permet a t_bateau de prendre sa bonne valeur 			
def aleatoireNavire(tab):
	n=6
	for i in range (1,6):
		for j in range (1,n-i):
			t_bateau = i
			placerNavire(tab, t_bateau)
	for i in range (15):
		for j in range (15):
			if tab[j][i] == 0 or tab[j][i] == 9:
				tab[j][i] = Back.CYAN + ' ' + Back.RESET
				
				
#############
#           #
#  PHASE 3  #
#           #
#############

#Fonction qui permet de compter combien il y a de morceaux de navire dans chaque colonne
def compteurColonne(tab,j):
	compteurColonne = 0
	for i in range (15):
		if tab[j][i] == Back.MAGENTA + ' ' + Back.RESET or tab[j][i] == Back.RED + ' ' + Back.RESET or tab[j][i] == Back.GREEN + ' ' + Back.RESET or tab[j][i] == Back.YELLOW + ' ' + Back.RESET :
			compteurColonne = compteurColonne + 1
	return compteurColonne
		
#Fonction qui permet de compter combien il y a de morceaux de navire dans chaque ligne		
def compteurLigne(tab,i):	
	compteurLigne = 0
	for j in range (15):
		if tab[j][i] == Back.MAGENTA + ' ' + Back.RESET or tab[j][i] == Back.RED + ' ' + Back.RESET or tab[j][i] == Back.GREEN + ' ' + Back.RESET or tab[j][i] == Back.YELLOW + ' ' + Back.RESET :
			compteurLigne = compteurLigne + 1
	return compteurLigne
	
#Fonction qui demande à l'utilisateur avec quel niveau de difficulté il veut jouer	
def nivDiff(tab,tabnoir):
	print(Fore.YELLOW + 'Bienvenue dans le jeu de la bataille navale solitaire.\n'+ Fore.RESET )
	regles()
	casecache = 0
	niv = saisirEntier(1,4,"Avec quel niveau de difficulté voulez-vous jouer ? Entrez:\n - 1 pour Facile (60 cases visibles)\n - 2 pour Moyen (40 cases)\n - 3 pour Difficile (20 cases)\n")
	#Le nombre de cases affichées dépend du niveau de diffiulté
	if niv == 1:
		niv = 60
	if niv == 2:
		niv = 40
	if niv == 3:
		niv = 20
	while casecache != niv:	
		i = randrange(15)
		j = randrange(15)
		if tabnoir[j][i] != tab[j][i] :
			tabnoir[j][i] = tab[j][i]
			casecache = casecache + 1	
	for i in range(16):
		for j in range(16):
			if tabnoir[j][i]==0:
				tabnoir[j][i]= Back.BLACK + ' ' + Back.RESET
	effacerEcran()
	afficherTab(tabnoir)
	
#Fonction qui permet la gestion d'erreur pour les nombres que doit saisir l'utilisateur
def saisirEntier(min,max,question):
	valide = False
	while (not valide):
		try:
			char=input(question)
			entier=int(char)
			if entier>= min and entier<max:
				valide=True
			else:
				print("Donner un entier entre",min,"et",max-1)
		except ValueError:
			print("Saisir un entier !!!")
	return entier
	
	
#############
#           #
#  PHASE 4  #
#           #
#############

#Fonction qui permet de proposer des actions à l'utilisateur
def choisiraction():
	print("Quelle action voulez-vous faire ? Entrez : \n")
	print(" - 1 pour un morceau de sous-marin :",1*(Back.MAGENTA + ' ' + Back.RESET + " "))
	print(" - 2 pour un morceau de torpilleur :",2*(Back.RED + ' ' + Back.RESET + " "))
	print(" - 3 pour un morceau d'escorteur :",3*(Back.GREEN + ' ' + Back.RESET + " "))
	print(" - 4 pour un morceau de croiseur :",4*(Back.YELLOW + ' ' + Back.RESET + " "))
	print(" - 5 pour un morceau de mer :",1*(Back.CYAN + ' ' + Back.RESET + " "))	
	print(" - 6 pour une ligne de mer")
	print(" - 7 pour une colonne de mer	")
	choixaction = saisirEntier(1,8,"")
	if choixaction == 1 or choixaction == 2 or choixaction == 3 or choixaction == 4 or  choixaction == 5 :
		resultat = choixmorbat(choixaction,choixbat)
	else:
		resultat = actionLigneColonne(choixaction)
	return resultat

#Fonction qui permet à l'utilisateur de choisir un morceau de bateau ou de mer sur la grille à l'aide des coordonnées	
def choixmorbat(choixaction, choixbat):
		case = gestionErreurCase("A quelle case ?(Tapez par exemple A1)", colonne)
		effacerEcran()
		y = int(colonne.index(case[0]))
		x = int(case[1:])
		#SOUS-MARIN
		if choixaction == 1 :
			resultat = choixbat(Back.MAGENTA + ' ' + Back.RESET, "sous-marin", x, y)
		#TORPILLEUR
		if choixaction == 2 :
			resultat = choixbat(Back.RED + ' ' + Back.RESET, "torpilleur", x, y)
		#ESCORTEUR
		if choixaction == 3 :
			resultat = choixbat(Back.GREEN + ' ' + Back.RESET, "escorteur", x, y)
		#CROISEUR
		if choixaction == 4 :
			resultat = choixbat(Back.YELLOW + ' ' + Back.RESET, "croiseur", x, y)
		#MER
		if choixaction == 5 :
			resultat = choixbat(Back.CYAN + ' ' + Back.RESET, "mer", x, y)
		return resultat
		
#Fonction qui permet de dire à l'utilisateur si il a bien trouvé un morceau de bateau ou si il s'est trompé		
def choixbat(couleur, bat, x, y):	
	if tab[y-1][x-1] == couleur:
		tabnoir[y-1][x-1] = tab[y-1][x-1]
		afficherTab(tabnoir)
		print(Fore.GREEN + "Bravo, vous avez trouvé un morceau de ", bat,"\n" + Fore.RESET)
		resultat = 1
	else:
		afficherTab(tabnoir)
		print(Fore.RED + "Dommage il n'y a pas de ",bat ,", vous ajoutez 10 points à votre score.\n" + Fore.RESET)
		resultat = 2
	return resultat
	
#Fonction qui permet à l'utilisateur de remplir une ligne ou une colonne entière de mer	
def actionLigneColonne(choixaction):
	if choixaction == 6:
		i = saisirEntier(1,16,"Sur quelle ligne pensez-vous qu'il y a de la mer ?")-1
		effacerEcran()
		a = 0
		for j in range (15):
			if tab[j][i] == Back.CYAN + ' ' + Back.RESET or tabnoir[j][i] == tab[j][i]:
				a = a+0
			else:
				a = a+1
		if a == 0:
			for j in range (15):
				tabnoir[j][i] = tab[j][i]
			afficherTab(tabnoir)
			print(Fore.GREEN + "Bravo, vous avez trouvé une ligne de mer.\n" + Fore.RESET)
			resultat = 1
		else:
			afficherTab(tabnoir)
			print(Fore.RED + "Dommage, il n'y a pas de ligne de mer ici, vous ajoutez 10 points a votre score.\n" + Fore.RESET)
			resultat = 2
		
	if choixaction == 7:
		z = input("Sur quelle colonne pensez-vous qu'il y a de la mer ?")
		effacerEcran()
		j = colonne.index(z)-1
		a = 0
		for i in range (15):
			if tab[j][i] == Back.CYAN + ' ' + Back.RESET or tabnoir[j][i] == tab[j][i]:
				a = a+0
			else:
				a = a+1
		if a == 0:
			for i in range (15):
				tabnoir[j][i] = tab[j][i]
			afficherTab(tabnoir)
			print(Fore.GREEN + "Bravo, vous avez trouvé une colonne de mer.\n" + Fore.RESET)
			resultat = 1
		else:
			afficherTab(tabnoir)
			print(Fore.RED + "Dommage, il n'y a pas de colonne de mer ici, vous ajoutez 10 points a votre score.\n" + Fore.RESET)
			resultat = 2
	return resultat			
			
			
#Fonction qui permet la gestion d'erreur des cases que doit saisir l'utilisateur
def gestionErreurCase(question, colonne):
	valide = False
	while (not valide):
		try:
			char=input(question)
			if char[1:] in ligne and char[0] in colonne:
				valide=True
			else:
				if char[1:] not in ligne:
					print("La ligne n'est pas correcte")
				if char[0] not in colonne:
					print("La colonne n'est pas correcte")
		except ValueError:
			print("Saisir une lettre et un chiffre")
	return char
			
#############
#           #
#  PHASE 5  #
#           #
#############

#Fonction qui permet le déroulement de la partie et le comptage du score
def partie(tab,tabnoir):
	a = 1
	score = 0
	while a != 0:
		a = 0
		resultat = choisiraction()
		for i in range (15):
			for j in range (15):
				if tab[j][i] == Back.MAGENTA + ' ' + Back.RESET or tab[j][i] == Back.RED + ' ' + Back.RESET or tab[j][i] == Back.GREEN + ' ' + Back.RESET or tab[j][i] == Back.YELLOW + ' ' + Back.RESET :
					if tabnoir[j][i] != tab[j][i]:
						a = a + 1
		if resultat == 1:
			score = score +1
		else : 
			score = score + 10
		print("Votre score est de :", score)
	print("Vous avez gagné !")
	
	
#############
#           #
#  PHASE 6  #
#           #
#############

#Fonction pour effacer l'écran sur le terminal	
def effacerEcran():
   print("\x1b[2J\x1b[H")
   
#Affichage des règles pour le joueur	
def regles():
	print("Le but du jeu est de trouver :\n")
	print("Un Croiseurs de 4 cases :",4*(Back.YELLOW + ' ' + Back.RESET + " "))
	print("Deux Escorteurs de 3 cases :",3*(Back.GREEN + ' ' + Back.RESET + " "))
	print("Trois Torpilleurs de 2 cases :",2*(Back.RED + ' ' + Back.RESET +" "))
	print("Quatre Sous-marin de 1 cases :",1*(Back.MAGENTA + ' ' + Back.RESET + " "))
	print("\n")
				
init()
effacerEcran()
aleatoireNavire(tab)
nivDiff(tab,tabnoir)
partie(tab,tabnoir)

