
#Package 3: Team Class:
#The Team class models a basketball team, encapsulating its name, wins, and losses. 
#It provides methods to manipulate these attributes and retrieve their values, 
#which allows for easy tracking of team performance throughout the basketball season.


def __init__(self, name, wins=0, losses=0):
    #Initializes a Team instance with the specified name, wins, and losses.
    
    #Constructor 
    #@param name String: The name of the team 
    #@param wins Integer: The number of Wins (default 0)
    #@param losses Integer: The number of losses (default 0)
    
    self._name = name 
    self._wins = wins
    self._losses = losses

def get_losses(self):
    
    #Getter
    #return intger: The number of losses for the current team 
    
    return self._losses

def set_losses(self, losses):
    
    #Gets the number of losses for the team 
    #@param losses integer: The number of losses to assign 
    
    self._losses = losses 

def change_name(self, new_name):
    
    #Change the name of the team 
    #@param new_name String: The new Team name
    
    self._name = new_name

def __str__(self):
    
    #return String: A redable representation of the current object
    

    return f"Team {self._name}: {self._wins} Wins, {self._losses} Losses"

def __repr__(self):
    
    #@return String: A string contatining code that can be
    # executed to create a copy of the current object
    

    return f"Team3('{self._name}', wins={self._wins}, losses={self._losses})"

