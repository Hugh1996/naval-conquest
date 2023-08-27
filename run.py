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

    def print_grid(self):
        """
        Prints the grid
        """
        print(f"{self.name}'s Grid:")
        for row in self.grid:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.grid[x][y] = "X"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.grid[x][y] = "S"

    def populate_grid(self):
        """
        Place ships randomly on the grid
        """
        while len(self.ships) < self.num_ships:
            x = random_point(self.size)
            y = random_point(self.size)
            if (x, y) not in self.ships:
                self.add_ship(x, y)

def random_point(size):
    """
    Returns random integer between 0 and size - 1
    """
    return randint(0, size - 1)

def valid_coordinates(x, y, grid):
    """
    Checks if x and y are valid on the grid
    Returns True if valid
    """
    try:
        self.grid[x][y]
        return True
    except IndexError:
        return False

def player_input(grid):
    """
    Get and process players input
    """
    while True:
        try:
            x = int(input("Guess a row: "))
            y = int(input("Guess a column: "))
            if valid_coordinates(x, y, grid):
                return x, y
            else:
                print("Invalid coordinates. Try again")
        except ValueError:
            print("Invalid input. Please enter numbers")

def play_game(computer_grid, player_grid):
    """
    Plays the game between player and computer
    """
    print(f"{player_grid.name}, choose your coordinates!")

def new_game():
    """
    Starts a new game. Sets the board size and number of ships.
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
    player_name = input("Please enter your name: \n")
    print("-" * 75)

    computer_grid = Grid(size, num_ships, "Computer", type="computer")
    player_grid = Grid(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_grid(player_grid)
        populate_grid(computer_grid)

    play_game(computer_grid, player_grid) # Initiates game loop

new_game() # Initiates new game
