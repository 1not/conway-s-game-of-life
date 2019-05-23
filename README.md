# Conway's Game of Life

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
The "game" is a zero-player game. It consists of a collection of cells which, based on a few mathematical rules, can live, die or multiply. Depending on the initial conditions, the cells form various patterns throughout the course of the game.
It is actually a simple and beautiful simulation of life's evolution, through mathematical rules.


The Rules

  For a space that is 'populated':
    Each cell with one or no neighbors dies, as if by solitude.
    Each cell with four or more neighbors dies, as if by overpopulation.
    Each cell with two or three neighbors survives.
    
  For a space that is 'empty' or 'unpopulated':
    Each cell with three neighbors becomes populated.


Many different types of patterns occur in the Game of Life, which are classified according to their behaviour. 
Common pattern types include: still lifes, oscillators, spaceships.
  Still lifes don't change from one generation to the next.
    Common examples: block, beehive, loaf, boat, tub.
  Oscillators return to their initial state after a finite number of generations.
    Common examples: blinker, toad, beacon, pulsar, pentadecathlon.
  Spaceships translate themselves across the grid.
    Common examples: glider, lightweight spaceship.
 
There are also some common structures, like "Gosper glider gun" which was explored by MIT team led by Bill Gosper.
But the true magic and enthusiasm in this game is in it's dynamical nature and infinite number of possibilities.
You create the world, let it breath and you don't know what you will see or when it will end. Maybe after 4 iterations, maybe after 4 million iterations, maybe never.
So, let's find out.

#Create Game of Life.exe:  pyinstaller -w -i /path_of_icon /path_of_gameoflife.py
#Create Game of Life.sh:  $ chmod +x /path_of_gameoflife.py
#Run the Game of Life
