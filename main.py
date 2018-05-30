from components.word import Word
from components.board import Board

def main():
    crossword = Board(5, 5)
    crossword.read_clues("questions.csv")
    crossword.print_board(True)
    crossword.print_clues()

if __name__ == "__main__":
    main()
