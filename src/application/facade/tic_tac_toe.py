#! /usr/bin/env python3

from src.application.services.game import marks
from src.application.services.game import movement
from src.application.services.board import board_base
from src.application.services.board import board_display
from src.application.services.board import free_fields
from src.application.extensions import console
from src.application.services.criteria import victory_check
from src.application.services.criteria import victory_definition

class Tic_Tac_Toe:

    __game_board = []

    def __game_board_movement(self, is_human_turn):
        """ Draws the movement according to the turn

            Parameters
            ----------
            human_turn : bool
                Indicates the turn, if True then it is the human turn, if False it is the machine turn.
        """

        game_board_tuple = movement.Movement().set_movement("human", __game_board) if is_human_turn else movement.Movement().set_movement("machine", __game_board) # create a tuple to represent the field that will be marked

        __game_board[game_board_tuple[0]][game_board_tuple[1]] = marks.Marks().get("human") if is_human_turn else marks.Marks().get("machine") # add mark in the field

        del game_board_tuple # delete tuple

    def game(self):
        """ Represents the Tic Tac Toe itself
        """

        global __game_board

        console.Console().clear()

        __game_board = board_base.Board_Base().empty_board()

        is_human_turn = False # define the first turn as the machine

        self.__game_board_movement(is_human_turn) # set the first machine movement

        free = free_fields.Free_Fields().make_list_of_free_fields(__game_board)

        is_human_turn = True # define the next turn as the human

        while len(free):
            console.Console().clear()

            board_display.Board_Display().display(__game_board)

            self.__game_board_movement(is_human_turn)

            if is_human_turn:
                victory = victory_definition.Victory_Definition().victory_for(__game_board,marks.Marks().get("human"))
            else: # machine turn
                victory = victory_definition.Victory_Definition().victory_for(__game_board,marks.Marks().get("machine"))
            if victory != None:
                break

            is_human_turn = not is_human_turn	

            free = free_fields.Free_Fields().make_list_of_free_fields(__game_board)

        console.Console().clear()

        board_display.Board_Display().display(__game_board)

        print(victory_check.Victory_Check().check_victory(victory))