from datetime import date

class Gazelle():
    """this is a class for all GAZELLE objects"""
    def __init__(self, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
class GazelleRefactored():
    """this is a class for all GAZELLE objects represented as STRINGS"""
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

    # refactor GAZELLE as a child class by adding (Animal)
class Gazelle(Animal):
    #remove redundant properties and set values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift   # stays on GAZELLE: not all animals have shifts
        self.walking = True  # Stays on GAZELLE: not all animals 'walk'
                   