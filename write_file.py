#!/usr/bin/python3
"""Module to write API key"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the
       number of characters written
    """
    with open(filename, 'w') as f:
        f.write(text)
