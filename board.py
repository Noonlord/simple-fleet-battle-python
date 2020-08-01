import numpy as np
class Board:
	def __init__(self):
		self.board = np.zeros((10, 10))
		self.opponentBoard = np.zeros((10, 10))
	def addShips(self):
		for i in range(5):
			notSet = True
			while notSet:
				print("Use x,y style coordinates")
				coordinates = input("Add {} unit vertical ship to: ".format(i + 1))
				x = int(coordinates.split(",")[0])
				y = int(coordinates.split(",")[1])
				counter = 0
				for j in range(i + 1):
					if self.board[y+j][x] == 0:
						print("{},{}".format(y+j,x))
						counter = counter + 1
					else:
						break
					if counter == (i + 1):
						for k in range(i + 1):
							self.board[y+k][x] = 1
						notSet = False
	def hit(self):
		hit = True
		while hit:
			print("Use x,y style coordinates")
			coordinates = input("Give coordinates to hit: ")
			x = int(coordinates.split(",")[0])
			y = int(coordinates.split(",")[1])
			if self.board[y][x] == 1:
				self.board[y][x] = -1
				print("It is a hit!")
				self.opponentBoard[y][x] = 1
			else:
				self.opponentBoard[y][x] = -1
				hit = False
