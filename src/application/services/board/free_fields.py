#! /usr/bin/env python3

from src.application.services.game import marks

class Free_Fields:
    
    def make_list_of_free_fields(self, board):
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
                if board[row][col] not in [marks.Marks().get("human"),marks.Marks().get("machine")]: # is the cell free?
                    free.append((row,col)) # yes, it is - append new tuple to the list
        return free