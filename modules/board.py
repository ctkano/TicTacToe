#! /usr/bin/env python3

""" module: board """

def display(board):
	""" Displays/Prints the current game board.

    	Parameters
        ----------
        game_board : list
            The game board.
	"""

	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def make_list_of_free_fields(board):
	""" Lists the free fields in the game board.

    	Parameters
        ----------
        game_board : list
            The game board.
		
		Returns
    	----------
		free : list
			The list of free fields in the game board.
	"""

	free = []	# the list is empty initially
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in ['O','X']: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free

def empty():
	""" Makes an empty game board.
		
		Returns
    	----------
		game_board : list
			A list that represents the game board.
	"""

	return [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
