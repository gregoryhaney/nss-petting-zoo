from datetime import date

class Koi():
    """this is a class for all KOI objects"""
    def __init__(self, name, species, food):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class KoiRefactored():
    """this is a class for all KOI objects represented as STRINGS"""
    # Initialize the items
    name = ""
    species = ""
    food = ""
    def __init__(self, name, species, food):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food    
        
    def __str__(self):
        return f"{self.name} is a {self.species}"
         