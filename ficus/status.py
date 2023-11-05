from ficus.row import RowInterface

class Status(RowInterface):
    def __init__(self, column_name, status_name, weight):
        self.__column_name = column_name
        self.__status_name = status_name
        self.__weight = weight
    
    @property
    def value(self):
        return self.__status_name
    
    @property
    def column_name(self):
        return self.__column_name
    
