#! /usr/bin/env python3

class Board_Base:

	def empty_board(self):
		""" Makes an empty game board.
			
			Returns
			----------
			game_board : list[list[int]]
				A list that represents the game board.
		"""

		return [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]