from datetime import date

class Leech():
    """this is a class for all LEECH objects"""
    def __init__(self, name, species, food):
        self.id = id
        self.name = name
        self.species = species
        self.slither = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
class LeechRefactored():
    """this is a class for all LEECH objects represented as STRINGS"""
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

# refactor LEECH as a child class by adding (Animal)
class Leech(Animal):
    #remove redundant properties and set values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slither = True  # Stays on LEECH: not all animals 'slither'
             