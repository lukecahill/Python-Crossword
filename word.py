class Word:
    letters = ""
    direction = ""
    start_pos = []  # first is across, second item is down

    def __init__(self, letters, direction, start_pos):
        self.letters = letters
        self.direction = direction
        self.start_pos = start_pos
