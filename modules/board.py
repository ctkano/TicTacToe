#! /usr/bin/env python3

""" module: board """

from modules import marks as mark

border = None
field = None
central_field_space = None
markMachine = None
markHuman = None

def display(board):
	""" Displays/Prints the current game board.

    	Parameters
        ----------
        game_board : list
            The game board.
	"""

	#region Board drawing
	global border
	global field
	global central_field_space

	if border is None:
		border = (("+" + "-" * 7) * 3) + "+" # define the border
	
	if field is None:
		field = (("|"+" " * 7) * 3) + "|" # define the field, below and above the central field

	if central_field_space is None:
		central_field_space = " " * 3 # dfine the central field spaces, in the left and right of the field value
	#endregion

	print(border, sep="")
	for row in range(3):
		print(field, sep="")
		for col in range(3):
			print("|", central_field_space, str(board[row][col]), central_field_space, sep="", end="")
		print("|")
		print(field,sep="")
		print(border,sep="")

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

	#region Marks
	global markMachine
	global markHuman

	if markMachine is None:
		markMachine = mark.machine()

	if markHuman is None:
		markHuman = mark.human()
	#endregion

	free = []	# the list is empty initially
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in [markHuman,markMachine]: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free

def empty():
	""" Makes an empty game board.
		
		Returns
    	----------
		game_board : list[list[int]]
			A list that represents the game board.
	"""

	return [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
