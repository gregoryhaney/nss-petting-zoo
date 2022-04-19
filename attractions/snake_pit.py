from . import Attraction

class SnakePit(Attraction):
    """This is the class for the SnakePit attraction"""
    def __init__(self, name, description):
        super().__init__(name, description)
        