from word import Word

board_height = 5
board_width = 5
board = [["[ ]"] * board_width for i in range(board_height)]

def print_board():
    for i in range(0, board_height):
        print("")
        for j in range(0, board_width):
            print(board[i][j], end='')

def add_word(new_word):
    if check_boundary(new_word) == False:
        print("That word is out of bounds!")
        return

    if check_position(new_word) == False:
        print("Could not add that word")
        return
    
    length = len(new_word.letters)
    if new_word.direction is "d":
        for i in range(0, length):
            board[new_word.start_pos[0] + i][new_word.start_pos[1]] = " {} ".format(new_word.letters[i])
    else:
        for i in range(0, length):
            board[new_word.start_pos[0]][new_word.start_pos[1] + i] = " {} ".format(new_word.letters[i])

def check_position(check_word):
    is_valid = True
    length = len(check_word.letters)
    for i in check_word.letters:
        if check_word.direction is "d":
            for j in range(0, length):
                # check if the item is empty and if not then if it's already the same
                print("i: {} j: {} ".format(i, j))
                if (board[j][check_word.start_pos[1]] != "[ ]") and (board[j][check_word.start_pos[1]] != i):
                   return False
        else:
            for j in range(0, length):
                if board[check_word.start_pos[0]][j] != i and board[check_word.start_pos[0]][j] != "[ ]":
                    return False
    return is_valid

def check_boundary(check_word):
    word_length = len(check_word.letters)
    x_coords = check_word.start_pos[1]
    y_coords = check_word.start_pos[0]
    direction = check_word.direction

    if direction is "d":
        if (y_coords + word_length) > board_height:
            return False
    else:
        if(x_coords + word_length) > board_width:
            return False
    return True

def main():
    add_word(Word("lol", "d", [0, 0]))
    print_board()
    print("")
    add_word(Word("nlp", "d", [0, 0]))  # this will not be added
    print_board()
    print("")
    add_word(Word("luke", "a", [4, 1]))
    print_board()
    print("")
    add_word(Word("areallylongone", "a", [1, 1]))   # this will also not be added
    print_board()
    print("")

if __name__ == "__main__":
    main()
