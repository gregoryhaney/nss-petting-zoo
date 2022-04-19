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
    
        # refactor KOI as a child class by adding (Animal)
class Koi(Animal):
    #remove redundant properties and set values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True  # Stays on Koi: not all animals 'swim'
      