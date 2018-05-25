class Board:
    height = 5
    width = 5
    board = []

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [["[ ]"] * width for i in range(height)]

    def print_board(self):
        for i in range(0, self.width):
            print("")
            for j in range(0, self.height):
                print(self.board[i][j], end='')
