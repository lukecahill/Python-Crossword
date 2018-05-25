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

def main():
    crossword = Board(5, 5)
    crossword.add_word_to_board(Word("lol", "d", [0, 0]))
    crossword.print_board(True)
    crossword.add_word_to_board(Word("let", "d", [0, 0]))  # this will not be added
    crossword.print_board(True)
    crossword.add_word_to_board(Word("luke", "a", [4, 1]))
    crossword.print_board(True)
    crossword.add_word_to_board(Word("let", "a", [0, 0]))
    crossword.print_board(True)
    crossword.add_word_to_board(Word("areallylongone", "a", [1, 1]))   # this will also not be added
    crossword.print_board(True)
    user_input_word()
    crossword.print_board(True)

if __name__ == "__main__":
    main()
