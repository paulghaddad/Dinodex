carnivores = ('Carnivore', 'Insectivore', 'Piscivore')

def biped(dinosaur):
    return dinosaur.walking == 'Biped'

def carnivore(dinosaur):
    if dinosaur.diet in carnivores:
        return True
    return False

def in_period(dinosaur, period):
    return bool(set(period) & dinosaur.period)

def of_size(dinosaur, size):
    if size == 'big':
        return dinosaur.big()
    else:
        return not dinosaur.big()
