import re

class UserInput:
    def user_input_word(self):
        while True:
            word_to_add = input("Enter a word to add: ")
            if not re.match("^[a-zA-Z]*$", word_to_add):
                print("Please only enter alphabetical letters")
            else:
                break
        return word_to_add

    def user_input_direction(self):
        while True:
            direction = input("Enter a direction ('d' or 'a'): ")
            if not re.match("^[adAD]{1}$", direction):
                print("Only 'a' or 'd' are valid choices")
            else:
                break
        return direction.lower()

    def user_input_coors(self, board):
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

    def user_guess_word(self):
        user_input = ""
        while True:
            user_input = input("Enter a guess: ")
            if re.match(" ", user_input):
                print("No whitespace allowed")
            else:
                break
        
        return user_input
