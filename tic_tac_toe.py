#! /usr/bin/env python3

""" module: main """

from sys import path
path.append('..\\modules')

import modules.board as board
import modules.movement as movement
import modules.criteria as criteria

game_board = board.empty()

human_turn = False

game_board_tuple = movement.machine(game_board) # get the first machine movement
game_board[game_board_tuple[0]][game_board_tuple[1]] = 'X'# set the first machine movement
del game_board_tuple

free = board.make_list_of_free_fields(game_board)

human_turn = True

while len(free):
	board.display(game_board)
	if human_turn:
		game_board_tuple = movement.user(game_board)
		game_board[game_board_tuple[0]][game_board_tuple[1]] = 'O'
		del game_board_tuple

		victory = criteria.victory_for(game_board,'O')
	else: #machine turn
		game_board_tuple = movement.machine(game_board)
		game_board[game_board_tuple[0]][game_board_tuple[1]] = 'X'
		del game_board_tuple

		victory = criteria.victory_for(game_board,'X')
	if victory != None:
		break
	human_turn = not human_turn		
	free = board.make_list_of_free_fields(game_board)

board.display(game_board)

print(criteria.check_victory(victory))

