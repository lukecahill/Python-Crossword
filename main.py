from components.board import Board
from components.user_input import UserInput

def main():
    crossword = Board(5, 5)
    user_input = UserInput()
    crossword.read_clues("questions.csv")
    crossword.print_board(True)
    crossword.print_clues()
    
    while True:
        guessed = user_input.user_guess_word()
        crossword.guess_word(guessed)
        crossword.print_board(True)

if __name__ == "__main__":
    main()
