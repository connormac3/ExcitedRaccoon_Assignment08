
class Team1:
    def __init__(self, name, wins=0, losses=0):
        self.name = name
        self._wins = wins
        self._losses = losses

    # Property for wins with getter and setter
    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, value):
        if value >= 0:
            self._wins = value
        else:
            raise ValueError("Wins cannot be negative")

    # Method to 'play a game' - adds a win or loss
    def play_game(self, result):
        if result.lower() == "win":
            self.wins += 1
        elif result.lower() == "lose":
            self._losses += 1

    # __str__ and __repr__ methods
    def __str__(self):
        return f"Team {self.name}: {self._wins} Wins, {self._losses} Losses"

    def __repr__(self):
        return f"Team1(name={self.name}, wins={self._wins}, losses={self._losses})"
