from . import Attraction

class WetLands(Attraction):
    """This is the class for the PettingZoo attraction"""
    def __init__(self, name, description):
        super().__init__(name, description)
        