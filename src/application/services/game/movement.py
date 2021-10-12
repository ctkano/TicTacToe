#! /usr/bin/env python3

from src.application.helper import movement_human
from src.application.helper import movement_machine

class Movement:

    def set_movement(self, type_of_turn, game_board):
        """ Set the movement for a given type of turn.

			Parameters
			----------
            type_of_turn : string
                The type of turn: Human or Machine

			game_board : list
				The game board.
			
			Returns
			----------
			game_board_tuple : tuple
                A tuple representing the row and the column representing 
                the movement according to the type of the turn.
                This tuple should be deleted after using it, otherwise, 
                the programmer must know or guess the new position of 
                the row and the column position inside this tuple.
		"""

        match type_of_turn.lower():
            case "machine":
                return movement_machine.Movement_Machine().move(game_board)
            case "human":
                return movement_human.Movement_Human().move(game_board)
            case _:
                raise ValueError('Definition not found.', 'class Movement', 'def set_movement()', 'argument type')