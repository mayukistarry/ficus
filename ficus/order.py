from ficus.row import RowInterface

class Orders:
    pass


# Orderは一行であることを意識して処理を書く
class Order(RowInterface):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size