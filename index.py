from animals import Goose
from attractions import PettingZoo
from attractions import SnakePit
from attractions import WetLands



bob = Goose("Bob", "Canadian Goose", "Watercress Sandwiches")
bob.run()
bob.swim()

varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)
    