from random import randint

class Grid:
    """
    Main grid class. Sets the grid size, 
    the number of ships, 
    the player's name and the board type
    Has methods for adding ships and guesses 
    and printing the board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.grid = [["." for x in range(size)] for y in range(size)] 
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []


