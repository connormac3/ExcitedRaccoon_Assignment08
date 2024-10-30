# main.py

# Name: Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: macfarct@mail.uc.edu, dewrm@gmail.com, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:   IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  
# Brief Description of what this module does: 
# Anything else that's relevant: 
# Citation: 



from team1Package.team1 import *
from team2Package.team2 import *
from team3Package.team3 import *

if __name__ == "__main__":

    def main():
        # Instantiate objects of each team
        team_a = Team1(name="Lions", wins=5, losses=3)
        team_b = Team2(name="Wolves", wins=6, losses=2)
        team_c = Team3(name="Hawks", wins=4, losses=4)

        # Demonstrate functionality and dunder methods

        # Team 1: Play game
        print(team_a)  # __str__ method
        team_a.play_game("win")
        print(f"After game, {team_a}")  # Updated wins

        # Team 2: Score points
        print(team_b)  # __str__ method
        print(team_b.score_points(120))

        # Team 3: Change team name
        print(team_c)  # __str__ method
        team_c.change_name("Eagles")
        print(f"Renamed team, {team_c}")  

        # Show repr for each team
        print(repr(team_a))
        print(repr(team_b))
        print(repr(team_c))
