#!/usr/bin/python3
"""
Module that defines the MyList class inheriting from list.
"""

class MyList(list):
    """Class that extends list with a method to print sorted elements."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        print(sorted(self))
