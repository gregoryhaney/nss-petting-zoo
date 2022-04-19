from asp import Asp
from bass import Bass
from cobra import Cobra
from cow import Cow
from gazelle import Gazelle
from guppy import Guppy
from koi import Koi
from leech import Leech
from moose import Moose
from oscar import Oscar
from reindeer import Reindeer
from salmon import Salmon
from slug import Slug
from wildebeast import Wildebeast
from worm import Worm
from datetime import date

class Animal():
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.data_added = date.today()
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')   
    
    @property     # the getter
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter     # the setter
    def chip_number(self, num):
        pass     # basically do nothing

# after refactoring, use these to build new objects:
mary = Moose("Mary", "Alaskan", "Midday")
marvin = Moose("Marvin", "Great North Mainer", "Morning")
warren = Wildebeast("Warren", "Hornless", "Morning")
winnie = Wildebeast("Winnie", "Domesticated", "Afternoon")
colton = Cow("Colton", "Holstein", "Afternoon")
cullen = Cow("Cullen", "Angus Bull", "Midday")
genny = Gazelle("Genny", "Longhaired", "Midday")
gary = Gazelle("Gary", "Canadian", "Morning")
rex = Reindeer("Rex", "Hairless", "Monring")
rudolph = Reindeer("Rudolph", "Red-nosed", "Afternoon")
edwin = Worm("Edwin", "Earthworm")
ned = Worm("Ned", "Nightcrawler")
silva = Slug("Silva", "Humpback Slug")
golda = Slug("Golda", "Garden Slug")
karen = Cobra("Karen", "Kalifornia King")
colby = Cobra("Colby", "Congo")
alice = Asp("Alice", "American Asian")
aaron = Asp("Aaron", "Black Mamba")
leo = Leech("Leo", "Anemic")
lawrence = Leech("Lawrence", "Saltwater")
steven = Salmon("Steven", "Rainbow Speckled")
sara = Salmon("Sara", "Murrel")
gayle = Guppy("Gayle", "Basking")
george = Guppy("George", "Flag Tail")
keith = Koi("Keith", "Barb Tail")
kevin = Koi("Kevin", "Neon Orange Glow")
oliver = Oscar("Oliver", "Beluga")
omar = Oscar("Omar", "Tuxedo Pink")
barry = Bass("Barry", "Small Mouth")
billy = Bass("Billy", "Large Mouth")
