class Dinosaur:
    BIG_WEIGHT_THRESHOLD = 2000

    def __init__(self, attributes):
        for attribute in attributes:
            setattr(self, attribute, attributes[attribute])

    def big(self):
        if not self.weight_in_lbs: return False
        return int(self.weight_in_lbs) > self.BIG_WEIGHT_THRESHOLD
