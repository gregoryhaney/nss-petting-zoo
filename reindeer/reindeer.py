from datetime import date

class Reindeer():
    """this is a class for all REINDEER objects"""
    def __init__(self, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class ReindeerRefactored():
    """this is a class for all REINDEER objects represented as STRINGS"""
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

    # refactor REINDEER as a child class by adding (Animal)
class Reindeer(Animal):
    #remove redundant properties and set values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift   # stays on REINDEER: not all animals have shifts
        self.walking = True  # Stays on REINDEER: not all animals 'walk'
            