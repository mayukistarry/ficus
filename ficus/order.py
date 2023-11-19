from ficus.row import RowInterface

class Order(RowInterface):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size