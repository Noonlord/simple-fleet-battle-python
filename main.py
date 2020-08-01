from board import Board
from os import system
p1Board = Board()
p2Board = Board()

input("Oyuncu 1 gemilerinizi ekleyin (enter tuşuna basın): ")
p1Board.addShips()
input("Ekranı temizlemek için entera basın: ")
system("clear")
input("Oyuncu 2 gemilerinizi ekleyin (enter tuşuna basın): ")
p2Board.addShips()
input("Ekranı temizlemek için entera basın: ")
system("clear")
isFinished = False
while True:
	input("Oyuncu 1, atış yap (enter tuşuna basın): ")
	isFinished = p2Board.hit()
	if isFinished == True:
		print("Oyuncu 1 kazandı")
		break
	input("Oyuncu 2, atış yap (enter tuşuna basın): ")
	isFinished = p1Board.hit()
	if isFinished == True:
		print("Oyuncu 2 kazandı")
		break
