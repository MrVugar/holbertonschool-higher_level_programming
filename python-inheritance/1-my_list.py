class MyList(list):
    """
    MyList class that inherits from list and includes a method to print sorted list.
    """
    def __init__(self):
        """Initializes the MyList object."""
        super().__init__()
    
    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
