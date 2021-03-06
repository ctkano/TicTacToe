#! /usr/bin/env python3

from src.application.services.game import marks

class Movement_Human:

	def move(self, game_board):
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
			ok = sign not in [marks.Marks().get("human"),marks.Marks().get("machine")] # symbols for the tic tac toe
			if not ok:	# it's already occupied - input another one again
				print("Field already occupied - enter your movement again!")
				continue
		return (row, col) # returns the tuple representing the row and the column
