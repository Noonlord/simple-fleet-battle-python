import numpy as np
class Board:
	def __init__(self):
		self.board = np.zeros((10, 10))
		self.opponentBoard = np.zeros((10, 10))
	def addShips(self):
		for i in range(5):
			notSet = True
			print("Use x,y style coordinates")
			while notSet:
				self.printBoard()
				coordinates = input("Add {} unit vertical ship to: ".format(i + 1))
				x = int(coordinates.split(",")[0])
				y = int(coordinates.split(",")[1])
				counter = 0
				for j in range(i + 1):
					try:
						if self.board[y+j][x] == 0:
							counter = counter + 1
						else:
							break
					except:
						break
					if counter == (i + 1):
						for k in range(i + 1):
							self.board[y+k][x] = 1
						notSet = False
	def hit(self):
		hit = True
		finished = False
		while hit:
			print("Use x,y style coordinates")
			self.printOpponent()
			coordinates = input("Give coordinates to hit: ")
			x = int(coordinates.split(",")[0])
			y = int(coordinates.split(",")[1])
			if self.board[y][x] == 1:
				self.board[y][x] = -1
				print("It is a hit!")
				self.opponentBoard[y][x] = 1
				finished = self.checkFinish()
				if finished:
					return True
			else:
				self.opponentBoard[y][x] = 9
				hit = False
		return False
	def printBoard(self):
		print("   0 1 2 3 4 5 6 7 8 9 ")
		print(" ")
		for i in range(10):
			lineToPrint = str(i) +  " "
			for j in range(10):
				lineToPrint = lineToPrint + " " + str(int(self.board[i][j]))
			print(lineToPrint)
	def printOpponent(self):
		print("   0 1 2 3 4 5 6 7 8 9 ")
		print(" ")
		for i in range(10):
			lineToPrint = str(i) +  " "
			for j in range(10):
				lineToPrint = lineToPrint + " " + str(int(self.opponentBoard[i][j]))
			print(lineToPrint)
	def checkFinish(self):
		isFinished = True
		for i in range(10):
			for j in range(10):
				if int(self.board[i][j]) == 1:
					isFinished = False
		return isFinished
