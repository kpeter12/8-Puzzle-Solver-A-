# Represents a board object, contains a list for the board and has functionality
# of an 8 puzzle
# Ex Board List: [1, 4, 2, 6, 0, 7, 8, 9, 3]
# represents:
# [1,4,2]
# [6,0,7]
# [8,5,3]
import random
import time


class Board:
    def __init__(self, board_list):
        random.seed(int(str(time.time_ns())[14]))
        self.board_list = board_list
        self.zero_location = board_list.index(0)
        self.available_moves = self.get_available_moves()        # eg: ['left', 'right', 'down']

    def __str__(self):
        s = str(self.board_list) + " | " + "Zero loc: " + str(self.zero_location) + " | Available Moves: " + str(self.available_moves)
        return s

    # moves the zero square in the direction given as the parameter, will update the class variables accordingly
    def move(self, direction):
        if direction == "None":
            return
        if direction not in self.available_moves:
            print("direction not in available moves for board")
            return
        else:
            if direction == "left":
                temp = self.board_list[self.zero_location-1]
                self.board_list[self.zero_location-1] = 0
                self.board_list[self.zero_location] = temp
                self.zero_location -= 1
            elif direction == "right":
                temp = self.board_list[self.zero_location + 1]
                self.board_list[self.zero_location + 1] = 0
                self.board_list[self.zero_location] = temp
                self.zero_location += 1
            elif direction == "up":
                temp = self.board_list[self.zero_location - 3]
                self.board_list[self.zero_location - 3] = 0
                self.board_list[self.zero_location] = temp
                self.zero_location -= 3
            elif direction == "down":
                temp = self.board_list[self.zero_location + 3]
                self.board_list[self.zero_location + 3] = 0
                self.board_list[self.zero_location] = temp
                self.zero_location += 3
        self.available_moves = self.get_available_moves()

    # updates the self.available_moves array to contain the current available moves
    def get_available_moves(self):
        avail_moves = []
        if self.zero_location > 2:
            avail_moves.append("up")
        if self.zero_location < 6:
            avail_moves.append("down")
        if self.zero_location != 0 and self.zero_location != 3 and self.zero_location != 6:
            avail_moves.append("left")
        if self.zero_location != 2 and self.zero_location != 5 and self.zero_location != 8:
            avail_moves.append("right")
        return avail_moves

    # shuffles the board for a certain amount of moves as specified by the moves parameter
    def shuffle_board(self, moves):
        for i in range(0, moves):
            d = random.choice(self.available_moves)
            self.move(d)


