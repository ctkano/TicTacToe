#! /usr/bin/env python3

""" module: criteria """

def victory_for(board,sign):
	""" Checks the victory and returns the winner (the user or the machine/computer)
		or None if the game is not ended.

    	Parameters
        ----------
        game_board : list
            The game field aka. the board game.
		sign : string
			The sign mark for the tic tac toe game, represented by: X or O

		Returns
    	----------
		who : string
			Who wins the game: the user or the machine/computer
			or None if the game is not ended.
	"""

	if sign == "X":	# are we looking for X?
		who = 'me'	# yes - it's machine's/computer's side
	elif sign == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:	# check row rc
			return who
		if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: # check column rc
			return who
		if board[rc][rc] != sign: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sign: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def check_victory(victory):
	""" Checks who is the winner and returns the text representing the victory status.

    	Parameters
        ----------
        victory : string
            Who is the winner.
		
		Returns
    	----------
		message : string
			The text representing the victory status.
	"""

	if victory == 'you':
		return "You won!"
	elif victory == 'me':
		return "I won"
	else:
		return "Tie!"
