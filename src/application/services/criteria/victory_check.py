#! /usr/bin/env python3

class Victory_Check:

    def check_victory(self, victory):
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
            return "\nYou won!\n"
        elif victory == 'me':
            return "\nI won\n"
        else:
            return "\nTie!\n"