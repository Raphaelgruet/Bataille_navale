from colorama import Style


#c'est pour effacer l'inviter de commande
def cls():
    print(Style.RESET_ALL)
    print("\x1b[2J\x1b[H",end="")
def posXY(x,y):
    print("\x1b["+str(y)+";"+str(x)+"H",end="")