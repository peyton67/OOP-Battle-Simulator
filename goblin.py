import random
from enemy import enemy

class Goblin(enemy):
    """
    This is our goblin blueprint 
    """
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
        print(f"Goblin {self.name} of {self.color} has entered the chat")
    

    
