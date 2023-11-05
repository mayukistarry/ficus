class ProportionalSequence:
    def __init__(self, a, b, size):
        self.__a = a
        self.__b = b
        self.__size = size
        self.__items = []
        for x in range(self.__size):
            self.__items.append(self.__a * x + self.__b)
    
    @property
    def items(self):
        return self.__items

class InverseProportinalSequence:
    def __init__(self, a, b, size):
        self.__a = a
        self.__b = b
        self.__size = size
        self.__items = []
        for x in range(self.__size):
            w = x + 1
            self.__items.append(self.__a / w + self.__b)
        
    @property
    def items(self):
        return self.__items

class QuadraticSequence:
    def __init__(self, a, b, c, size):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__size = size
        self.__items = []
        for x in range(self.__size):
            self.__items.append(self.__a * x ** 2 + self.__b * x + self.__c)
    
    @property
    def items(self):
        return self.__items

class InverseQuadraticSequence:
    def __init__(self, a, b, c, size):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__size = size
        self.__items = []
        for x in range(self.__size):
            w = x + 1
            self.__items.append(self.__a / w ** 2 + self.__b / w + self.__c)
    
    @property
    def items(self):
        return self.__items