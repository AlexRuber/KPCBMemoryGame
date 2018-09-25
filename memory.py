#!/usr/bin/env python
#memory.py

"""Python script for KPCB Memory game
<----------------------------------------------------------------------------->
Do not exceed 80 columns in any line 
<----------------------------------------------------------------------------->
This script runs the memory game assigned by the KPCB Engineering Application

"""
__program__ = 'Memory Game'
__author__  = 'Alex Ruber'
__version__ = '0.2'

# Import Declarations #
import os
import sys
import random
import time
import unittest
from datetime import datetime

# Methods #

#Define Boards - Hidden and Answer
def createBoard():
	# Global Variables
	global board
	global answer

	board = list("****************")
	board = [board[:4], board[4:8], board[8:12], board[12:]]

	#Define Answer board
	answer = list("KKkkPPppCCccBBbb")
	random.shuffle(answer)
	answer = [answer[:4], answer[4:8], answer[8:12], answer[12:]]
	
def startGame():
	# Define Global Start Time
	global startTime
	startTime = datetime.now()
	createBoard()
	updateAndShowBoard()
	while pickTile():
		pass

# User picks the tile coordinate
def pickTile():
	# Do not allow First and Second pick to be the same
	while True:
		a,b = map(int, raw_input('First pick: '))

		#try catch to check if pick is in range
		try:
			firstPick = answer[a][b]
			if board[a][b]=='*':
				updateAndShowBoard((a,b))
				break
			else:
				print("Can not pick same spot twice, pick again.") 

		# Handle throws list index out of range exception
		except IndexError:
			print("Uh oh, your coordinate is not on the board, try again!")
	
	# Do not allow First and Second pick to be the same
	while True:
		x,y = map(int, raw_input('Second pick: '))

		try:
			secondPick = answer[x][y]
			if board[x][y]=='*' and (a!=x or b!=y):
				break
			else:
				print("Can not pick same spot twice, pick again.") 
		
		except IndexError:
			print("Uh oh, your coordinate is not on the board, try again!")

	updateAndShowBoard((a,b),(x,y))
	time.sleep(0.25)

	# Match Case, remove both tiles from board
	if firstPick == secondPick:
		print("We have a match!")
		board[a][b] = answer[a][b]
		board[x][y] = answer[x][y]
		board[a][b] = ' '
		board[x][y] = ' '
	# No Match Case, flip both tiles
	else:
		print("No match") 
	
	# If there is still an asterisk, continue
	if any('*' in row for row in board):
		return True
	# If no asterisks are left, user has won
	else:
		endTime = datetime.now()
		yourTime = endTime - startTime
		print("Congratulations, your time was %s seconds!"
			% yourTime.seconds)
		newGame = raw_input("Would you like to play again: Y or N?")
		if newGame == "Y" or newGame == "y":
			startGame()
		else:
			print("Bye, thanks for playing!")

# Updates and shows the board
# Paramater: Takes in arbitrary number of picks, either one or two
def updateAndShowBoard(*picks):
	for row in range(len(answer)):
		for column in range(len(answer[0])):
			if (row,column) in picks:
				print answer[row][column],
			else:
				print board[row][column],
		print

# Unit Tests #
class MemoryTests(unittest.TestCase):
    def testUpdateAndShowBoard(self):
        self.assertEqual(updateAndShowBoard(01), 0)


# Call to Main #
if __name__ == '__main__':
	unittest.main()
	startGame()


