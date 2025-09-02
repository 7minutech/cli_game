import random

def hit_roll(percentage):
    if percentage > 100.0:
        return False
    return random.randint(1,100) <= (percentage * 100)