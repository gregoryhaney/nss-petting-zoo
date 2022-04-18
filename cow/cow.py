from datetime import date

class Cow():
    """this is a class for all COW objects"""
    def __init__(self, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class CowRefactored():
    """this is a class for all COW objects represented as STRINGS"""
    # Initialize the items
    name = ""
    species = ""
    food = ""
    shift = ""
    def __init__(self, name, species, shift, food, chip_num):
        self.id = id
        self.name = name
        self.species = species
        self.shift = shift
        self.slither = True
        self.food = food
        self.chip_number = chip_num
        
    @property      # the getter
    def chip_number(self):
        try:
            return self.__chip_number
        except AttributeError:
            return 0
    @chip_number.setter    # the setter
    def chip_number(self, chip_num):
        pass   # do nothing, which prevents the setting of a value
        
    def __str__(self):
        return f"{self.name} is a {self.species}"
               