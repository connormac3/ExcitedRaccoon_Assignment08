#Team2

class Team2:
    def __init__(self, name, wins=0, losses=0):
        self.name = name
        self._wins = wins
        self._losses = losses

    # Property for losses with getter and setter
    @property
    def losses(self):
        return self._losses

    @losses.setter
    def losses(self, value):
        if value >= 0:
            self._losses = value
        else:
            raise ValueError("Losses cannot be negative")

    # Method to score points
    def score_points(self, points):
        return f"Team {self.name} scored {points} points!"

    # __str__ and __repr__ methods
    def __str__(self):
        return f"Team {self.name}: {self._wins} Wins, {self._losses} Losses"

    def __repr__(self):
        return f"Team2(name={self.name}, wins={self._wins}, losses={self._losses})"

