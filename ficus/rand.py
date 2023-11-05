import random

class Random:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        
        self.__small_literal = 'abcdefghijklmnopqrstuvwxyz'
        self.__large_literal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__char_literal = self.__small_literal + self.__large_literal
        self.__number_literal = '0123456789'
        self.__symbol_literal = '!@#$%^&*()_+-=[]{};:,./<>?'
        self.__charnumber_literal = self.__char_literal + self.__number_literal
        self.__letter = self.__char_literal + self.__number_literal + self.__symbol_literal
    
    def randint(start, end):
        return random.randint(start, end)
    
    def randfloat(start, end):
        return random.uniform(start, end)
    
    def rand_lower_char(self):
        return random.choice(self.__small_literal)
    
    def rand_upper_char(self):
        return random.choice(self.__large_literal)
    
    def rand_char(self):
        return random.choice(self.__char_literal)
    
    def rand_letter(self):
        return random.choice(self.__letter)