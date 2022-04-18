class VarmintVillage():
    """This is the class for the entire Theme Park"""
    def __init__(self, park_area):
        self.id = id
        self.park_area = park_area

class PettingZoo():
    """This is the class for the PettingZoo attraction"""
    def __init__(self):
        self.id = id
        self.attraction_name = "Petting Zoo"
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()
    @property     # the getter
    def last_critter_added(self):
        last_animal = list[-1]
        return f'{last_animal}'
                  
class SnakePit():
    """This is the class for the SnakePit attraction"""
    def __init__(self):
        self.id = id
        self.attraction_name = "Snake Pit"
        self.description = "stupendous snakes and other slitherers"
        self.animals = list()
    @property     # the getter
    def last_critter_added(self):
        last_animal = list[-1]
        return f'{last_animal}'
        
class WetLands():
    """This is the class for the WetLands attraction"""
    def __init__(self):
        self.id = id
        self.attraction_name = "Wet Lands"
        self.description = "critters that love the water"
        self.animals = list()       
    @property     # the getter
    def last_critter_added(self):
        last_animal = list[-1]
        return f'{last_animal}'    
           
        
    def __str__(self):
        for attraction in VarmintVillage:
            print(f'{self.attraction_name} is where you can find {self.description}, like')
            for animal in PettingZoo.animals:
              print(f'{self.name} the {self.species}') 
        
 
    