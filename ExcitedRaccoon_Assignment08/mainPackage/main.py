# main.py

# Name: Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: macfarct@mail.uc.edu, dewrm@gmail.com, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:   IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborating with a team to create a basketball tournament with teams winning and loosing, then a name change for one of the teams. 
# Brief Description of what this module does: this is the entry point code that instatiates basketball teams then invokes methods. and it prints what happens to each team.
# Anything else that's relevant: 
# Citation: https://diveintopython.org/learn/classes/object-instantiation, used in class vehicle class as reference 

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
        print("After game:" , team_a)  # Updated wins

        # Team 2: Score points
        print(team_b)  
        team_b.score_points(120)

        # Team 3: Change team name
        print(team_c)  
        team_c.change_name("Eagles")
        print("Renamed team:", team_c)  

        # Show repr for each team
        print("Team 1:", (team_a))
        print("Team 2:", (team_b))
        print("Team 3:", (team_c))

if __name__ == "__main__":
    main()
