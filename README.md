# Naval Conquest: BattleGrid
Naval Conquest: BattleGrid is a Python terminal game experience, accessible through Heroku.

The objective is for players to beat the computer by successfully sinking all of the computer's battleships before their own battleships are discovered. 

Each individual battleship is confined to a single square on the game grid. 

[View the live version here](https://naval-conquest-30afa5133057.herokuapp.com/).

![Responsive](./images/responsive.jpg)

## How to Play

 - The player enters their name and two grids are randomly generated. By default, the grid dimensions stand at 5x5, housing a total of 4 battleships. Flexibility is embedded, allowing players to adjust both the grid size and the number of battleships according to their preference.

 - The player can see the location of their battleships, indicated by an 's' for ship. The computer's battleship positions remain concealed from the player.

 -  Instances of missed shots or inaccurate guesses are marked with 'x', whereas accurate hits are celebrated with '*'.

 - In a turn-based manner, players and the computer alternate, attempting to sink the others battleships.

 - Victory is achieved upon successfully sinking all of the opponents battleships.

 ## Features