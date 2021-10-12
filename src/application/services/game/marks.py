#! /usr/bin/env python3

class Marks:

    __mark = {"machine":"X","human":"O"} # Mark dictionary
    __markMachine = None
    __markHuman = None

    def __set(self):
        """ Set game marks
        """

        global __markMachine
        global __markHuman

        #region Marks
        if self.__markMachine is None:
            self.__markMachine = self.__mark["machine"]

        if self.__markHuman is None:
            self.__markHuman = self.__mark["human"]
        #endregion

    def get(self, mark_for):
        """ Get game marks for a given movement type

            Parameters
            ----------
            mark_for : string
                Indicates who is making the move: Human or Machine.
                Acceptable types:
                    * Human
                    * Machine
            
            Returns
    	    ----------
            mark : string
                The respective mark for the given movement type: Human or Machine.
        """

        self.__set()

        match mark_for.lower():
            case "machine":
                return self.__markMachine
            case "human":
                return self.__markHuman
            case _:
                raise ValueError('Definition not found.', 'class Marks', 'def get()', 'argument mark_for')