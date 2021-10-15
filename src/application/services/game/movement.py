#! /usr/bin/env python3

from src.application.helper.movement import movement_human, movement_machine
from src.application.services.game import marks

class Movement:

    def set_movement(self, is_human_turn, game_board):
        """ Set the movement for a given type of turn.

			Parameters
			----------
            is_human_turn : bool
                The type of turn: Human or Machine.
                If True, it is the human turn.
                If False, it is the machine turn.

			game_board : list
				The game board.
			
			Returns
			----------
			game_board : list
                The updated game board with the movement of the current turn.
		"""

        game_board_tuple = movement_human.Movement_Human().move(game_board) if is_human_turn else movement_machine.Movement_Machine().move(game_board) # create a tuple to represent the movement of the turn

        mark_for = "human" if is_human_turn else "machine" # define the type of mark: Human or Machine

        game_board[game_board_tuple[0]][game_board_tuple[1]] = marks.Marks().get(mark_for) # add mark in the field

        del game_board_tuple # delete tuple

        return game_board