# Naval Conquest: BattleGrid
Naval Conquest: BattleGrid is a Python terminal game experience, accessible through Heroku.

The objective is for players to beat the computer by successfully sinking all of the computer's battleships before their own battleships are discovered. 

Each individual battleship is confined to a single square on the game board. 

[View the live version here](https://naval-conquest-30afa5133057.herokuapp.com/).

![Responsive](./images/responsive.jpg)

## How to Play

 - The player enters their name and two boards are randomly generated. 

 - The player can see the location of their battleships, indicated by an 's' for ship. 

 -  Instances of missed shots or inaccurate guesses are marked with 'x', whereas accurate hits are celebrated with '*'.

 - In a turn-based manner, players and the computer alternate, attempting to sink the others battleships.

 - Victory is achieved upon successfully sinking all of the opponents battleships.

 ## Features

- ### Difficulty Selection

  - Players can choose the game's difficulty. 
  - The default board dimensions are set at 5x5, accomodating 4 battleships.
  - Flexibility is integrated, enabling players to customize the grid size and the number of battleships. 
  - Each selection influences the game's difficulty and duration. 

- ### Random Board Generation 

  - The game employs a randomly generated board.
  - Ships are placed randomly on the board for both the player and the computer.
  - Players are presented with these boards before selecting their target coordinates. 
  - The computer's battleship positions are kept concealed from the player. 

 ![Stage 1 of Game](./images/first.jpg)

- Gameplay

  - The player competes against the computer. 
  - The game accepts input from the player and keeps track of the score. 

- Player Input 

  - The player can input their desired coordinates by specifying the numbered row and column, both starting from 0.
  - Both the player's and computer's selected coordinates are displayed.
  - A message indicates whether the player or the computer has hit or missed a target.

- Scoring

  - Scores are updated and displayed after each round. 
  -  The score incrments by 1 when a target is successfully hit. 

- Round Progression

  - Players can proceed to the next round by pressing any key.
  - Alternatively, they can exit the game by pressing 'n'. 

 ![Stage 2 of Game](./images/two.jpg)

- Grid Display

  - Players are presented with updated grids prior to selecting new coordinates. 

- Hit Markings

  - Missed hits are indicated with an 'x', while succesful hits are marked with a '*'.

 ![Stage 3 of Game](./images/three.jpg)

### Features left to implement

## Data Model

- A Grid class was use as my model. I opted for Grid as opposed to Board, given the name of the game is Naval Conquest: BattleGrid. Two instances of a board are created, one for the player and one for the computer. 

- The Grid class stores board size, the numer of ships, player's name and the board type. 

- The class also has helper functions which are listed below. 

  - The 'print_grid' method prints the current board. 
  - The 'guess' method handle's the players guess and updates the board. 
  - The 'add_ship' method places the battleships on the x, y axis. 
  - The 'populate_grid' method places ships on the board. 

## Testing

 - I've given invalid inputs (strings, decimal number, same input twice) to ensure to player is prompted to enter the correct input. 
 - Tested in both my local terminal and Heroku. 

### Bugs

#### Solved Bugs

 - When running the game, I was getting KeyError for the player name that was input. I discovered this was due to calling player type as opposed to player_name variable. 

#### Unfixed Bugs

### Validator Testing

The code was passed thorugh a PEP8 linter and confirmed there are no problems. 

## Deployment

This project was deployed using Code Instiute's template for Heroku. To deploy, follow the below steps.

- Clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in that order
- Set a config var for KEY : VALUE to PORT : 8000
- Link the Heroku app to the repository
- Click on 'Deploy'

## Credits

- Code Institute for the deployment Terminal
- The sample Ultimate Battleship game for inspiration on the layout and structure of the game and code. 