import numpy as np
class Board:
	def __init__(self):
		self.board = np.zeros((10, 10))
		self.opponentBoard = np.zeros((10, 10))
