# Name: Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: macfarct@mail.uc.edu, dewrm@gmail.com, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:   IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborating with a team to create a basketball tournament with teams winning and loosing, then a name change for one of the teams. 
# Brief Description of what this module does: 
# Anything else that's relevant: 
# Citation: 

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

