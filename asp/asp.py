from datetime import date

class Asp():
    """this is a class for all ASP objects"""
    def __init__(self, name, species, food):
        self.id = id
        self.name = name
        self.species = species
        self.slither = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class AspRefactored():
    """this is a class for all ASP objects represented as STRINGS"""
    # Initialize the items
    name = ""
    species = ""
    food = ""
    def __init__(self, name, species, food):
        self.id = id
        self.name = name
        self.species = species
        self.slither = True
        self.food = food    
        
    def __str__(self):
        return f"{self.name} is a {self.species}"

class Asp(Animal):
    #remove redundant properties and set values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, chip_num)
        self.slither = True  # Stays on ASP: not all animals 'slither'
        self.food = food
 
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} after the {self.food} was chilled and mixed with hot salsa')
            