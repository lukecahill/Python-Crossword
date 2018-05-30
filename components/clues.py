class Clues:
    letters = ""
    direction = ""
    start_pos = []  # first is across, second item is down
    clue = ""

    def __init__(self, letters, clue, direction, start_pos):
        self.letters = letters
        self.direction = direction
        self.start_pos = start_pos
        self.clue = clue
