#! /usr/bin/env python3

""" module: console """

import os

def clear():
    """ Clear the console.
        When is a Windows OS it will be used the command cls
        When different than Windows OS, it will be used the command clear
	"""
    os.system('cls' if os.name=='nt' else 'clear')