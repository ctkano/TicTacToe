#! /usr/bin/env python3

import os

class Console:
    
    def clear(self):
        """ Clear the console.
            When is a Windows OS it will be used the command cls
            When different than Windows OS, it will be used the command clear
        """
        os.system('cls' if os.name=='nt' else 'clear')