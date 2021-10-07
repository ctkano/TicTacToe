#! /usr/bin/env python3

""" module: main """

import sys
sys.path.append('..\\modules')

import modules.board as board
import modules.marks as mark
import modules.movement as movement
import modules.criteria as criteria
import modules.console as console

markMachine = None
markHuman = None
game_board = []

def load_marks():
	""" Loads the game marks
	"""

	global markMachine
	global markHuman

	#region Marks
	if markMachine is None:
		markMachine = mark.machine()

	if markHuman is None:
		markHuman = mark.human()
	#endregion

def game_board_movement(human_turn):
	""" Draws the movement according to the turn

		Parameters
        ----------
        human_turn : bool
            Indicates the turn, if True then it is the human turn, if False it is the machine turn.
	"""

	load_marks()

	game_board_tuple = movement.user(game_board) if human_turn else movement.machine(game_board) # create a tuple to represent the field that will be marked

	game_board[game_board_tuple[0]][game_board_tuple[1]] = markHuman if human_turn else markMachine # add mark in the field

	del game_board_tuple # delete tuple

def game():
	""" Represents the Tic Tac Toe itself
	"""

	global game_board

	console.clear()

	game_board = board.empty()

	load_marks()

	human_turn = False # define the first turn as the machine

	game_board_movement(human_turn) # set the first machine movement

	free = board.make_list_of_free_fields(game_board)

	human_turn = True # define the next turn as the human

	while len(free):
		console.clear()

		board.display(game_board)

		game_board_movement(human_turn)

		if human_turn:
			victory = criteria.victory_for(game_board,markHuman)
		else: # machine turn
			victory = criteria.victory_for(game_board,markMachine)
		if victory != None:
			break

		human_turn = not human_turn	

		free = board.make_list_of_free_fields(game_board)

	console.clear()

	board.display(game_board)

	print(criteria.check_victory(victory))

def start():
	""" Starts the game
	"""

	try:
		game() # call the game
		
		reset = input("Do you want to play again? Type Y for Yes or N for No and the game will end: ")

		if reset.upper() == "Y" or reset.upper() == "YES":
			start() # restart the game
		else:
			sys.exit() # exit system
	except KeyboardInterrupt:
		print("\nToo bad you don't want to keep playing...\n")
		sys.exit() # exit system

"""
	Starts the game!!!
"""
start()