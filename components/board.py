from components.clues import Clues

import csv

class Board:
    height = 5
    width = 5
    board = []
    clues = []
    remaining = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [["[ ]"] * width for i in range(height)]

    def print_board(self, line_break = False):
        print(" ± ", end = "")
        for i in range(self.width):
            print(" {} ".format(i), end = "")
        board = [["[ ]"] * self.width for i in range(self.height)]

        for clue in self.clues:
            word_length = len(clue.letters)
            for letter in range(0, word_length):
                if clue.direction == "d" and not clue.hidden:
                    board[clue.start_pos[0] + letter][clue.start_pos[1]] = " {} ".format(clue.letters[letter])
                elif clue.direction == "d" and clue.hidden:
                    board[clue.start_pos[0] + letter][clue.start_pos[1]] = " X "
                elif clue.direction == "a" and not clue.hidden:
                    board[clue.start_pos[0]][clue.start_pos[1] + letter] = " {} ".format(clue.letters[letter])
                elif clue.direction == "a" and clue.hidden:
                    board[clue.start_pos[0]][clue.start_pos[1] + letter] = " X "
        
        for i in range(0, self.height):
            print("")
            print(" {} ".format(i), end = "")
            for j in range(0, self.width):
                if board[i][j] != "[ ]":
                    print(board[i][j], end = "")
                else:
                    print("[ ]", end = "")

        if line_break:
            print("")
            
    def add_word_to_board(self, new_word):
        if self.check_boundary(new_word) == False:
            print("The word '{}' is out of bounds!".format(new_word.letters))
            return

        if new_word.hidden == True:
            if self.check_position(new_word) == False:
                print("Could not add word: '{}'".format(new_word.letters))
                return
        
        length = len(new_word.letters)
        if new_word.direction is "d":
            for i in range(0, length):
                if new_word.hidden:
                    self.board[new_word.start_pos[0] + i][new_word.start_pos[1]] = " {} ".format("X")
                else:
                    self.board[new_word.start_pos[0] + i][new_word.start_pos[1]] = " {} ".format(new_word.letters[i].lower())
        else:
            for i in range(0, length):
                if new_word.hidden:
                    self.board[new_word.start_pos[0]][new_word.start_pos[1] + i] = " {} ".format("X")
                else:
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
                self.remaining = self.remaining + 1

    def print_clues(self):
        clues_length = len(self.clues)
        for clue in range(0, clues_length):
            print("Clue number {}: Down {}, Across {}. {}".format(clue, self.clues[clue].start_pos[0], self.clues[clue].start_pos[1], self.clues[clue].clue))

    def guess_word(self, guessed_word, guess_number):
        correct = False
        item = self.clues[guess_number]
        if item.letters == guessed_word:
            item.hidden = False
            self.add_word_to_board(item)
            print("{} was a correct guess.".format(guessed_word))
            correct = True
            self.remaining = self.remaining - 1
            return self.is_game_won()
    
        if not correct:
            print("{} was a wrong guess.".format(guessed_word))
        
        return False

    def is_game_won(self):
        if self.remaining == 0:
            return True
        else:
            return False
