import random

class Random:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
    
    def randint(start, end):
        return random.randint(start, end)
    
    def randfloat(start, end):
        return random.uniform(start, end)