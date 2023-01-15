
class Coordonnee:

	__x = 0
	__y = 0
	__z = 0

	def __init__(self, x, y, z):
		self.__x = x
		self.__y = y
		self.__z = z

	def setWithArray(self, coordonnee):
		self.__x = int(coordonnee[0])
		self.__y = int(coordonnee[1])
		self.__z = int(coordonnee[2])

	def __str__(self):
		return str([self.__x,self.__y,self.__z])

	def __eq__(self, other):
		if other.getX() == self.getX() and other.getY() == self.getY() and other.getZ() == self.getZ():
			return True
		else:
			return False

	def __hash__(self):
		# Method de hashage
		#return int(self.__str__())
		return int(str(self.__x)+str(self.__y)+str(self.__z))

	# COORDONNEE X

	def setX(self, value):
		self.__x = value

	def increaseX(self):
		self.__x += 1

	def decreaseX(self):
		self.__x -= 1

	def getX(self):
		return self.__x

	# COORDONNEE Y

	def setY(self, value):
		self.__y = value

	def increaseY(self):
		self.__y += 1

	def decreaseY(self):
		self.__y -= 1

	def getY(self):
		return self.__y

	#COORDONNEE Z

	def setZ(self, value):
		self.__z = value

	def increaseZ(self):
		self.__z += 1

	def decreaseZ(self):
		self.__z -= 1

	def getZ(self):
		return self.__z

	def emplacementCoordonnee(self):
	# Permet de donner la position sur le plateau d'une coordonnée

		for i in range (10):
			if self.__x == i+1:
				x=8+i*5
		for j in range (3):
			if self.__z == j+1:
				x = x+60*j
		for k in range(5):
			if self.__y == k+1:
				y =6+3 * k
		return x, y