class Drink:
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
def getName(): Drink.name

def setName(name):
    Drink.__name__ = name
