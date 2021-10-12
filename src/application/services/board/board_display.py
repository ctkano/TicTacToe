#! /usr/bin/env python3

class Board_Display:

    __border = None
    __field = None
    __central_field_space = None

    def display(self, board):
        """ Displays/Prints the current game board.

            Parameters
            ----------
            game_board : list
                The game board.
        """

        #region Board drawing
        global __border
        global __field
        global __central_field_space

        if self.__border is None:
            self.__border = (("+" + "-" * 7) * 3) + "+" # define the border
        
        if self.__field is None:
            self.__field = (("|"+" " * 7) * 3) + "|" # define the field, below and above the central field

        if self.__central_field_space is None:
            self.__central_field_space = " " * 3 # dfine the central field spaces, in the left and right of the field value
        #endregion

        print(self.__border, sep="")
        for row in range(3):
            print(self.__field, sep="")
            for col in range(3):
                print("|", self.__central_field_space, str(board[row][col]), self.__central_field_space, sep="", end="")
            print("|")
            print(self.__field,sep="")
            print(self.__border,sep="")