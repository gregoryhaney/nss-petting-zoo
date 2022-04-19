from .animal import Animal
from movements import Walking, Swimming

class Goose(Animal, Walking, Swimming):
    def __init__(self, name, species, food):
        # no more "super()" when initializing multiple base classes
        Animal.__init__(self, name, species, food)
        Swimming.__init__(self)
        Walking.__init__(self)
        
    def honk(self):
        print("The goos honks.")
    
    def run(self):
        print(f'{self} waddles')
        
    def __str__(self):
        return f'{self.name} the Goose'
  