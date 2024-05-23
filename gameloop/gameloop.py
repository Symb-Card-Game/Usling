
class Game:
    def __init__(self) -> None:
        self.turn_counter = 0

    def next_turn(self):
        self.turn_counter += 1