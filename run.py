from random import randint

scores = {"computer": 0, "player": 0}

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

    def print_grid(self)
    """
    Prints the grid
    """
    for row in self.grid:
        print("".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.grid[x][y] = "X"

        if (x, y) in self.ships:
            self.grid[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def random_point(self, size):
        """
        Returns random integer between 0 and size - 1
        """
        return randint(0, size - 1)

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error. You cannot add more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player"
            self.grid[x][y] = "S"

    def new_game(self)
    """
    Starts a new_game. Sets the board size and number of ships.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 75)
    print("Welcome to Naval Conquest: BattleGrid")
    print("Sink or be sunk - the choice is yours! Are you ready to conquer the seas?")
    print(f"Grid Size: {size}\nNumber of Ships: {num_ships}")
    print("-" * 75)
    name = input("Please enter your name: \n")

    computer_grid = Grid(size, num_ships, "Computer", type="computer")
    player_grid = Grid(size, num_ships, player_name, type="computer")

new_game()