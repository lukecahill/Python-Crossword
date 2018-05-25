from components.word import Word
from components.board import Board
import re

def user_input_word():
    while True:
        word_to_add = input("Enter a word to add: ")
        if not re.match("^[a-zA-Z]*$", word_to_add):
            print("Please only enter alphabetical letters")
        else:
            break
    return word_to_add

def user_input_direction():
    while True:
        direction = input("Enter a direction ('d' or 'a'): ")
        if not re.match("^[ad]*$", direction):
            print("Only 'a' or 'd' are valid choices")
        else:
            break
    return direction

def user_input_coors(board):
    coordinates = []

    while True:
        coord_to_add = input("Enter a starting Y coordinate (0 to {}): ".format(board.height - 1))
        if not re.match("^[0-9]*$", coord_to_add):
            print("Please only enter numbers")
        else:
            coordinates.append(int(coord_to_add))
            break

    while True:
        coord_to_add = input("Enter a starting X coordinate (0 to {}): ".format(board.width - 1))
        if not re.match("^[0-9]*$", coord_to_add):
            print("Please only enter numbers")
        else:
            coordinates.append(int(coord_to_add))
            break
    return coordinates


def main():
    crossword = Board(5, 5)
    # crossword.add_word_to_board(Word("lol", "d", [0, 0]))
    # crossword.print_board(True)
    # crossword.add_word_to_board(Word("let", "d", [0, 0]))  # this will not be added
    # crossword.print_board(True)
    # crossword.add_word_to_board(Word("luke", "a", [4, 1]))
    # crossword.print_board(True)
    # crossword.add_word_to_board(Word("let", "a", [0, 0]))
    # crossword.print_board(True)
    # crossword.add_word_to_board(Word("areallylongone", "a", [1, 1]))   # this will also not be added
    # crossword.print_board(True)
    word = user_input_word()
    coordinates = user_input_coors(crossword)
    direction = user_input_direction()
    crossword.add_word_to_board(Word(word, direction, coordinates))
    crossword.print_board(True)

if __name__ == "__main__":
    main()
