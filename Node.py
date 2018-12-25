# A node will represent a board state.
# It contains an array with the current board state as well as some other attributes used by A*.
from Board import Board
from bisect import bisect_left


class Node:
    def __init__(self, board_object, parent, g, direction):
        self.board = board_object     # board object
        self.board.move(direction)
        self.parent = parent          # parent node
        self.g = g + 1                # g(n): cost of path so far, 1 for each move
        self.h = self.heuristic()     # h(n): estimated cost to the goal, using Manhattan Distance. !!!!!!!!!!
        self.f = self.g + self.h      # f(n): g(n) + h(n). This is the criteria by which the frontier is ordered
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def __str__(self):
        s = "NODE: " + str(self.board) + " | f(n): " + str(self.f) + " | d: " + str(self.depth)
        return s

    def __eq__(self, other):
        if self.board.board_list == other.board.board_list:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.board.board_list < other.board.board_list

    def __le__(self, other):
        return self.board.board_list <= other.board.board_list

    def expand_node(self, open_list, closed_list):
        for direc in self.board.available_moves:
            n = Node(Board(self.board.board_list.copy()), self, self.g, direc)
            if n not in closed_list:
                open_list.append(n)

    # returns the h(x) value for the manhattan distance
    def heuristic(self):
        goal_board_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        manhattan_distance = 0
        for i in range(0, len(self.board.board_list)):
            index_of_i = self.board.board_list.index(i)
            distance = abs(index_of_i - i)
            if distance > 5:
                manhattan_distance += 2
            elif distance > 2:
                manhattan_distance += 1
            manhattan_distance += abs(index_of_i - i) % 3

        n_seq = 0
        for i in range(0, len(self.board.board_list)):
            if i == 4:
                n_seq += 1
            elif self.board.board_list[i] != goal_board_list[self.clock_wise(i)]:
                n_seq += 2
            return n_seq + manhattan_distance

    #returns the index clockwise to the given index
    def clock_wise(self, index):
        if index == 0 or index == 1:
            return index + 1
        elif index == 2 or index == 5:
            return index + 3
        elif index == 8 or index == 7:
            return index - 1
        elif index == 3 or index == 6:
            return index - 3
        elif index == 4:
            return 4
        # [0, 1, 2,
        #  3, 4, 5,
        #  6, 7, 8]

