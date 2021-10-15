#! /usr/bin/env python3

from src.application.services.game import marks
from src.application.services.game import movement
from src.application.services.board import board_base
from src.application.services.board import board_display
from src.application.services.board import free_fields
from src.application.extensions import console
from src.application.services.game_over import winning_criteria
from src.application.services.game_over import winning_message

class Tic_Tac_Toe:

    __game_board = []

    def game(self):
        """ Represents the Tic Tac Toe itself
        """

        global __game_board

        console.Console().clear() # clear the console

        __game_board = board_base.Board_Base().empty_board() # create an empty board

        is_human_turn = False # define the first turn as the machine

        __game_board = movement.Movement().set_movement(is_human_turn, __game_board) # set the first machine movement

        free = free_fields.Free_Fields().make_list_of_free_fields(__game_board) # list free fields

        is_human_turn = True # define the next turn as the human

        while len(free):
            console.Console().clear() # clear the console

            board_display.Board_Display().display(__game_board) # display updated board

            __game_board = movement.Movement().set_movement(is_human_turn, __game_board) # make the movement

            mark_for = "human" if is_human_turn else "machine"  # define the type of mark: Human or Machine
            
            victory = winning_criteria.Winning_Criteria().check_victory_for(__game_board,marks.Marks().get(mark_for)) # check victory
            
            if victory != None:
                break # someone won

            is_human_turn = not is_human_turn # change the turn

            free = free_fields.Free_Fields().make_list_of_free_fields(__game_board) # list free fields

        console.Console().clear() # clear the console

        board_display.Board_Display().display(__game_board) # display updated board

        print(winning_message.Winning_Message().check_victory_message(victory)) # print the victory message
        
        if(len(free_fields.Free_Fields().make_list_of_free_fields(__game_board)) > 0):
            print("Flawless victory!!!\n") # print the flawless victory message