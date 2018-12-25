**Introduction**
The 8 Puzzle Problem involves a board with nine squares. Eight of the squares hold a number and one of the squares is a free space. The goal is to end up with all the squares on the board in order starting at one and ending at eight, with the last square of the board being the free space.

The challenge of the puzzle is that the player cannot “pickup” or swap two numbered squares. The player can only move blocks into the free space. The player must keep rearranging blocks into the free space until the board has successfully reached the goal state.

In order to get a computer to solve the 8 Puzzle, this program implemented the A* search algorithm. A* is an algorithm that is commonly used for tree or graph traversal because it is complete and is an optimal algorithm if the heuristic function used is admissible.

**Environment**
Python 3.7
Modules: time, random, sys, tkinter (for graphics)

**Implementation**
The Heuristic function I used was the Manhattan Distance. This is calculated by calculating the distance (rows + cols) of each number from its goal position.

**Usage**
Running the program with no command line arguments will present the user with a graphical user interface where the user can enter his own start board or choose a randomly shuffled board.
The program will solve the board and then present the user with a step by step visual representation of the path to the goal board state.
If the program is run with command line arguments, the graphics will be disabled. The program takes only 1 command line argument with the number of shuffles for the starting board.