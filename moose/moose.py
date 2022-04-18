from datetime import date

class Moose():
    """this is a class for all MOOSE objects"""
    def __init__(self, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class MooseRefactored():
    """this is a class for all MOOSE objects represented as STRINGS"""
    # Initialize the items
    name = ""
    species = ""
    food = ""
    shift = ""
    def __init__(self, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.shift = shift
        self.slither = True
        self.food = food    
        
    def __str__(self):
        return f"{self.name} is a {self.species}"
                