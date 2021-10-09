#! /usr/bin/env python3

""" module: movement """

from random import randrange
from modules import board
from modules import marks as mark

markMachine = None
markHuman = None

def user(game_board):
	""" Gets the user's input and check the game field availability for the movement.
		If available returns the tuple representing the row and the column selected for the movement.
		Otherwise, if not available, it will inform the user to select another game field.

    	Parameters
        ----------
        game_board : list
            The game board.
		
		Returns
    	----------
		game_board_tuple : tuple
			A tuple representing the row and the column.
			This tuple should be deleted after using it, otherwise, 
			the programmer must know or guess the new position of 
			the row and the column position inside this tuple.
	"""

	#region Marks
	global markMachine
	global markHuman

	if markMachine is None:
		markMachine = mark.machine()

	if markHuman is None:
		markHuman = mark.human()
	#endregion

	ok = False	# fake assumption to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - enter your movement again!") # no, it isn't - input another one
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = game_board[row][col]	# check the selected position
		ok = sign not in [markHuman,markMachine] # symbols for the tic tac toe
		if not ok:	# it's already occupied - input another one again
			print("Field already occupied - enter your movement again!")
			continue
	return (row, col) # returns the tuple representing the row and the column

def machine(game_board):
	""" Randomly generates the machine/computer movement and 
		returns the tuple representing the row and the column.

    	Parameters
        ----------
        game_board : list
            The game board.
		
		Returns
    	----------
		game_board_tuple : tuple
			A tuple representing the row and the column.
			This tuple should be deleted after using it, otherwise, 
			the programmer must know or guess the new position of 
			the row and the column position inside this tuple.
	"""
	
	free = board.make_list_of_free_fields(game_board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	# if the list is not empty, choose a place for the machine movement and set it
            this = randrange(cnt)
            row, col = free[this]
            return (row, col) # returns the tuple representing the row and the column