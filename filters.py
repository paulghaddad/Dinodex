carnivores = ('Carnivore', 'Insectivore', 'Piscivore')

def biped(dinosaur):
    return dinosaur.walking == 'Biped'

def carnivore(dinosaur):
    if dinosaur.diet in carnivores:
        return True
    return False

def in_period(dinosaur, period):
    return bool(period & dinosaur.period)

