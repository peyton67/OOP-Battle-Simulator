import random
from enemy import enemy

class boss(enemy):
    def __init__(self, name):
        super().__init__(name)
        self.color = "red"
        self.name = name
        print(f"The big boss called {self.name} is {self.color} and has entered the chat")
        self.health = 674167
        self.attack_power = 670

    def attack(self):
        if self.health < 6767: 
            self.attack = 1000
        elif self.health < 3000:
            self.attack_power = 5000
            print("NO MORE MR. NICE GUY.")
        return self.attack_power
    
