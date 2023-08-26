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
            self.grid[x][y] = "*"
            return "Hit"
        else:
            self.grid[x][y] = "X"
            return "Miss"

    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error. You cannot add more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.grid[x][y] = "S"

    def random_point(self):
        """
        Returns random integer between 0 and size - 1
        """
        return randint(0, self.size - 1)

    def valid_coordinates(self, x, y):
        """
        Checks if x and y are valid on the grid
        Returns True if valid
        """
        try:
            self.grid[x][y]
            return True
        except IndexError:
            return False

    def populate_grid(self):
        """
        Place ships randomly on the grid
        """
        for _ in range(self.num_ships):
            x, y = self.random_point(), self.random_point()
            while (x, y) in self.ships:
                x, y = self.random_point(), self.random_point()
            self.add_ship(x, y)

    def play_game(computer_grid, player_grid):
        """
        Plays the game between player and computer
        """
        print(f"{player_grid.name}, choose your coordinates!")
        while True:
            player_x = int(input("Enter row:"))
            player_y = int(input("Enter column:"))
            if player_grid.valid_coordinates(player_x, player_y) and (player_x, player_y) not in player_grid.guesses:
                break
            else:
                print("Input must be between 0 and 4")

        result = computer_grid.guess(player_x, player_y)
        if result == "Hit":
            scores["player"] += 1

        print("Computer's Turn:")
        while True:
            computer_x = computer_grid.random_point()
            computer_y = computer_grid.random_point()
            if (computer_x, computer_y) not in computer_grid.guesses:
                break

            result = player_grid.guess(computer_x, computer_y)
            if result == "Hit":
                scores["computer"] += 1

            print("Player's Grid:")
            player_grid.print_grid()
            print("Computer's Grid:")
            computer_grid.print_grid()

        if scores["player"] == computer_grid.num_ships:
            print("Congratulations! You win!")
        else:
            print("Computer wins! Better luck next time!")

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

    player_grid.populate_grid() # Populates player ships randomly on grid
    computer_grid.populate_grid() # Populates computer ships randomly on grid

    player_grid.print_grid() # Print player grid
    computer_grid.print_grid() # Prints computer grid

    player_grid.play_game(player_grid) # Initiates game loop

new_game() # Initiates new game
