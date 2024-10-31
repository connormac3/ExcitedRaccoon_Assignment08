# teamMachup


# Name: Ryan Dew
# email: dewrm@mail.uc.edu
# Assignment Number: 08
# Due Date:  10/31/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This is a team assignment that we are told to collaborate on a python project, we chose to create a sports team matchup program. We have 3 classes 1 for team wins and losses, 1 for total points score and 1 change team name.

# Brief Description of what this module does. This module is a class that models a team matchup, including the opponent's name and the location of the game. It provides methods to get and set these attributes, print matchup details, and represent the object as a string.
# Citations:   https://realpython.com/python-getter-setter/ --> getter and setter reference \\ https://www.datacamp.com/tutorial/elif-statements-python --> If, elif statement put in, that we used InClass assignment for reference

# Anything else that's relevant: None

class Team1(object):
    """
    Model a sports team with a name, win count, and loss count.
    """
    
    def __init__(self, name, wins=0, losses=0):
        """
        Constructor
        @param name String: The name of the team
        @param wins Integer: Initial wins for the team (default is 0)
        @param losses Integer: Initial losses for the team (default is 0)
        """
        self.__name = name
        self.__wins = wins
        self.__losses = losses

    def get_name(self):
        """
        @return String: The name of the team
        """
        return self.__name
    
    def set_name(self, name):
        """
        Set the team name
        @param name String: The new team name
        """
        if name:
            self.__name = name
        else:
            raise ValueError("Team name cannot be empty.")

    def get_wins(self):
        """
        @return Integer: The win count of the team
        """
        return self.__wins

    def set_wins(self, wins):
        """
        Set the win count for the team
        @param wins Integer: The new win count, must be non-negative
        """
        if wins >= 0:
            self.__wins = wins
        else:
            raise ValueError("Wins cannot be negative.")

    def get_losses(self):
        """
        @return Integer: The loss count of the team
        """
        return self.__losses

    def set_losses(self, losses):
        """
        Set the loss count for the team
        @param losses Integer: The new loss count, must be non-negative
        """
        if losses >= 0:
            self.__losses = losses
        else:
            raise ValueError("Losses cannot be negative.")

    def play_game(self, result):
        """
        Update the team's record by adding a win or a loss based on the game result
        @param result String: The result of the game, either 'win' or 'lose'
        """
        if result.lower() == "win":
            self.set_wins(self.get_wins() + 1)
        elif result.lower() == "lose":
            self.set_losses(self.get_losses() + 1)
        else:
            raise ValueError("Result must be 'win' or 'lose'.")

    def print_record(self):
        """
        Print the team's current win-loss record
        """
        print(f"Team {self.__name}: {self.__wins} Wins, {self.__losses} Losses")
        
    def __str__(self):
        """
        @return String: A human-readable representation of the team and its record
        """
        return f"Team {self.__name}: {self.__wins} Wins, {self.__losses} Losses"

    def __repr__(self):
        """
        @return String: A string that can be evaluated to recreate the object
        """
        return f"Team1(name='{self.__name}', wins={self.__wins}, losses={self.__losses})"
    
