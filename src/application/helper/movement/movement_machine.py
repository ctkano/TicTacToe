#! /usr/bin/env python3

from random import randrange
from src.application.services.board import free_fields

class Movement_Machine:

    def move(self, game_board):
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
        
        free = free_fields.Free_Fields().make_list_of_free_fields(game_board) # make a list of free fields
        cnt = len(free)
        if cnt > 0:	# if the list is not empty, choose a place for the machine movement and set it
                this = randrange(cnt)
                row, col = free[this]
                return (row, col) # returns the tuple representing the row and the column