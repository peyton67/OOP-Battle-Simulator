import random
from enemy import enemy

class boss:
    def __init__(self, name,color):
        super().__init__(name)
        self.color = "red"
        self.name = "Super mean boss stinky pants"
        print(f"The big boss called {self.name} is {self.color} and has entered the chat")
