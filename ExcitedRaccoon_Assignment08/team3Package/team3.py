

class Team3:
    def __init__(self, name, wins=0, losses=0):
        self.name = name
        self._wins = wins
        self._losses = losses

    # Property for name with getter and setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    # Method to change team name
    def change_name(self, new_name):
        self.name = new_name

    # __str__ and __repr__ methods
    def __str__(self):
        return f"Team {self.name}: {self._wins} Wins, {self._losses} Losses"

    def __repr__(self):
        return f"Team3(name={self.name}, wins={self._wins}, losses={self._losses})"
