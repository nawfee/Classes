import random

class Agent():
    
    def __init__ (self, y, x):
        print("construct agent")
        self.y = y
        self.x = x
        pass

    '''
    def __init__ (self):
        print("construct agent")
        self.x = 1
        pass
    '''
    
    def hi(self):
        print("Hello")
        
    def move(self):
        if random.random() < 0.5:
            self.y  = (self.y  + 1) % 100
        else:
            self.y  = (self.y  - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
