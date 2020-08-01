from board import Board
from os import system
p1Board = Board()
p2Board = Board()

input("Player 1 add your ships (press enter): ")
p1Board.addShips()
input("Press enter to clear screen: ")
system("clear")
input("Player 2 add your ships (press enter): ")
p2Board.addShips()
input("Press enter to clear your screen: ")
system("clear")
isFinished = False
while True:
	input("Player 1 make a hit (press enter): ")
	isFinished = p2Board.hit()
	if isFinished == True:
		print("Player 1 wins")
		break
	input("Player 2 make a hit (press enter): ")
	isFinished = p1Board.hit()
	if isFinished == True:
		print("Player 2 wins")
		break
