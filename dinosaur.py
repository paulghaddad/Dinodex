class Dinosaur:
    def __init__(self, attributes):
        for attribute in attributes:
            setattr(self, attribute, attributes[attribute])
