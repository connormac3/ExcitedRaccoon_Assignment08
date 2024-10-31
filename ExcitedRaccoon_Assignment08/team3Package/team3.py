
#Package 3: Team Class:

# Name: JD Pointdexter
# email:poindejd@mail.uc.edu
# Assignment Number: 08
# Due Date:  10/31/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment:Collaborating with a team to create a basketball tournament with teams winning and loosing, then a name change for one of the teams. 
# Brief Description of what this module does: The Team class models a basketball team, encapsulating its name, wins, and losses. 
#It provides methods to manipulate these attributes and retrieve their values, which allows for easy tracking of team performance throughout the basketball season.
# Citations https://www.w3schools.com/python/python_classes.asp, https://stackoverflow.com/questions/22517885/how-to-create-a-python-class, https://www.geeksforgeeks.org/getter-and-setter-in-python/

class Team3(object):
    '''
     Initializes a Team instance with the specified name, wins, and losses.
    '''
    def __init__(self, name, wins=0, losses=0):
       
        '''
        Constructor 
        @param name String: The name of the team 
        @param wins Integer: The number of Wins (default 0)
        @param losses Integer: The number of losses (default 0)
        '''
        self._name = name 
        self._wins = wins
        self._losses = losses

    def get_losses(self):
        '''
        Getter
        return intger: The number of losses for the current team 
        '''
        return self._losses

    def set_losses(self, losses):
        '''
        Gets the number of losses for the team 
        @param losses integer: The number of losses to assign 
        '''
        self._losses = losses 

    def change_name(self, new_name):
        '''
        Change the name of the team 
        @param new_name String: The new Team name
        '''
        self._name = new_name

    def __str__(self):
        '''
        return String: A redable representation of the current object
        '''

        return f"Team {self._name}: {self._wins} Wins, {self._losses} Losses"

    def __repr__(self):
        '''
        @return String: A string contatining code that can be
        executed to create a copy of the current object
        '''

        return f"Team3('{self._name}', wins={self._wins}, losses={self._losses})"

