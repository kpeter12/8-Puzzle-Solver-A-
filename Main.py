# This program solves an 8 board represented by an array using the A* algorithm
from Node import Node
from Board import Board
from Graphics2 import Graphics2
from Gui import Gui
from queue import PriorityQueue
import time

closed_list = []      # list implementation of closed list
open_list = []          # list implementation for open list

gu = Gui()

goal_board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])      # final state that we want the board to be
start_board = Board(gu.get_board())     # this will be the board that is later shuffled and put into CL
root_node = Node(start_board, None, -1, "None")
# shuffle board based off of command line arg
print("Starting Board:", root_node.board)

g = Graphics2(root_node.board.board_list)

time1 = time.time()
closed_list.append(root_node)
current_node = root_node

found_node = False
while not found_node > 0:
    # check for goal
    print(closed_list[-1])
    g.update_main_board(closed_list[-1].board.board_list)
    if closed_list[-1].board.board_list == goal_board.board_list:
        found_node = True
        print("FOUND GOAL \n", closed_list[-1], "\n", "PATH")
        # generate path to goal
        path_to_goal = []
        current_node = closed_list[-1]
        while current_node.parent is not None:
            path_to_goal.insert(0, current_node)
            current_node = current_node.parent
        path_to_goal.insert(0, current_node)
        # for debugging, print path_to_goal
        for item in path_to_goal:
            print(item)

        g.update_main_board(closed_list[-1].board.board_list)
        print("V:", len(closed_list))
        print("Time Taken: ", time.time() - time1)
        g.show_solution(path_to_goal)
        exit(0)
    # if goal has not been found
    else:
        current_node = closed_list[-1]
        #closed_list.sort(key=lambda x: x.board.board_list)
        current_node.expand_node(open_list, closed_list)
        open_list.sort(key=lambda x: x.f)  # sort open list by f(n) value
        closed_list.append(open_list[0])
        del open_list[0]

