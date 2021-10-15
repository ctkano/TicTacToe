#! /usr/bin/env python3

import sys
from datetime import date
from src.application.facade import tic_tac_toe as tictactoe

class Start:
	def now(self):
		""" Starts the game
		"""

		try:
			tictactoe.Tic_Tac_Toe().game() # call the Tic Tac Toe game
			
			# If today is Friday, then display a special message
			if date.today().weekday() == 4:
				print("Yeah ... Today is finally Friday!!! C'mon consider this in the decision below...", end="\n\n")

			reset = input("Do you want to play again? Type Y or YES to continue (case insensitive): ")

			if reset.upper() == "Y" or reset.upper() == "YES":
				self.now() # restart the game
			else:
				sys.exit() # exit system
		except KeyboardInterrupt:
			print("\nToo bad you don't want to keep playing...\n")
			sys.exit() # exit system