from components.word import Word
from components.clues import Clues

import csv

class Board:
    height = 5
    width = 5
    board = []
    clues = []

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [["[ ]"] * width for i in range(height)]

    def print_board(self, line_break = False, hidden = False):
        for i in range(0, self.height):
            print("")
            for j in range(0, self.width):
                print(self.board[i][j], end='')

        if line_break:
            print("")
            
    def add_word_to_board(self, new_word):
        if self.check_boundary(new_word) == False:
            print("The word '{}' is out of bounds!".format(new_word.letters))
            return

        if self.check_position(new_word) == False:
            print("Could not add word: '{}'".format(new_word.letters))
            return
        
        length = len(new_word.letters)
        if new_word.direction is "d":
            for i in range(0, length):
                self.board[new_word.start_pos[0] + i][new_word.start_pos[1]] = " {} ".format(new_word.letters[i].lower())
        else:
            for i in range(0, length):
                self.board[new_word.start_pos[0]][new_word.start_pos[1] + i] = " {} ".format(new_word.letters[i].lower())

    def check_position(self, check_word):
        is_valid = True
        length = len(check_word.letters)
        starting_position = check_word.start_pos
        for i in range(length):
            if check_word.direction is "d":
                y_board_pos = self.board[i + starting_position[0]][starting_position[1]]
                if y_board_pos != "[ ]" and y_board_pos != " {} ".format(check_word.letters[i]):
                    return False    # return False straight away to avoid un-needed loop cycles
            else:
                x_board_pos = self.board[starting_position[0]][i + starting_position[1]]
                if x_board_pos != "[ ]" and x_board_pos != " {} ".format(check_word.letters[i]):
                    return False
        return is_valid

    def check_boundary(self, check_word):
        word_length = len(check_word.letters)
        x_coords = check_word.start_pos[1]
        y_coords = check_word.start_pos[0]
        direction = check_word.direction

        if direction is "d":
            if (y_coords + word_length) > self.height:
                return False
        else:
            if (x_coords + word_length) > self.width:
                return False
        return True

    def read_clues(self, file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                clue = Clues(row[0], row[1], row[2], [int(row[3][0]), int(row[3][-1])])
                self.clues.append(clue)
                self.add_word_to_board(clue)
