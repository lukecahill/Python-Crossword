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
        if guessed == ":q":
            break
        has_user_won = crossword.guess_word(guessed)
        crossword.print_board(True)
        crossword.print_clues()
        
        if has_user_won:
            print("Congratulations you have won!")
            break

if __name__ == "__main__":
    main()
