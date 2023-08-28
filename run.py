import random
from random import randint

# Keeps track of player's scores
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
            print("".join(row))

    def guess(self, x, y):
        """
        Handles player's guess and updates the grid
        """
        if (x, y) in self.guesses:
            return "Already guessed!"

        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.grid[x][y] = "*"
            return "Successful Hit!"
        else:
            self.grid[x][y] = "x"
            return "Missed!"

    def add_ship(self, x, y, type="computer"):
        """
        Places ships on x, y axis
        """
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add more ships!")
        else:
            # Add the ship's coordinates to the lsit of ships
            self.ships.append((x, y))
            if self.type == "player":
                # If player, marks the grid cell with an "S" for ship
                self.grid[x][y] = "s"

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
    Returns random integer within grid size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, grid):
    """
    Checks if coordinates are within grid boundaries
    """
    try:
        grid.grid[x][y]
        return True
    except IndexError:
        return False


def player_input(grid):
    """
    Get and validates player's input
    """
    while True:
        try:
            x = int(input("Guess a row: "))
            y = int(input("Guess a column: "))
            if valid_coordinates(x, y, grid):
                return x, y
            else:
                print("Invalid coordinates. Input must be between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game(computer_grid, player_grid):
    """
    Executes game loop
    Players take turn making guesses
    Grid and scores updated accordingly
    """
    print("-" * 75)
    print(f"{player_grid.name}, it's time to attack!")

    while True:
        print("-" * 75)
        player_grid.print_grid()
        print("-" * 75)
        computer_grid.print_grid()

        while True:
            player_x, player_y = player_input(player_grid)

            if (player_x, player_y) in player_grid.guesses:
                print("You've already guessed those coordinates. Try again!")
            else:
                player_grid.guesses.append((player_x, player_y))
                break

        player_guess_result = computer_grid.guess(player_x, player_y)
        print(f"{player_grid.name} guessed: ({player_x}, {player_y})")
        print(f"{player_grid.name} {player_guess_result}")

        computer_x, computer_y = (
            random_point(computer_grid.size),
            random_point(computer_grid.size)
        )
        computer_guess_result = player_grid.guess(computer_x, computer_y)
        print(f"Computer guessed: ({computer_x}, {computer_y})")
        print(f"Computer {computer_guess_result}")

        if player_guess_result == "Successful Hit!":
            scores["player"] += 1
        elif player_guess_result == "Missed!":
            scores["player"] += 0

        if computer_guess_result == "Successful Hit!":
            scores["computer"] += 1
        elif computer_guess_result == "Missed!":
            scores["computer"] += 0

        print("-" * 75)
        print(f"After this round, the scores are: ")
        print(f"{player_grid.name}: {scores['player']} "
              f"Computer: {scores['computer']}")
        print("-" * 75)

        continue_playing = input("Enter any key to continue or 'n' to quit:")
        if continue_playing.lower() == 'n':
            break

        print("Keys in scores dictionary:", scores.keys())


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
    print("Sink or be sunk - the choice is yours! Ready to conquer the seas?")
    print(f"Grid Size: {size}\nNumber of Ships: {num_ships}")
    print("-" * 75)
    player_name = input("Please enter your name: \n")
    print("-" * 75)

    computer_grid = Grid(size, num_ships, "Computer", type="computer")
    player_grid = Grid(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        player_grid.populate_grid()
        computer_grid.populate_grid()

    # Initiates game loop
    play_game(computer_grid, player_grid)


# Initiates new game
new_game()