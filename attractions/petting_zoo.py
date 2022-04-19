from . import Attraction

class PettingZoo(Attraction):
    """This is the class for the PettingZoo attraction"""
    def __init__(self, name, description):
        super().__init__(name, description)
        