class Dinosaur:
    BIG_WEIGHT_THRESHOLD = 2000

    def __init__(self, attributes):
        self.name = attributes.get('name')
        self.period = list(attributes.get('period'))
        self.continent = attributes.get('continent')
        self.diet = attributes.get('diet')
        self.weight = attributes.get('weight')
        self.walking_mode = attributes.get('walking_mode')
        self.description = attributes.get('description')

    def big(self):
        if not self.weight: return False
        return int(self.weight) > self.BIG_WEIGHT_THRESHOLD
