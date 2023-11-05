from ficus.row import RowInterface

class Statuses:
    def __init__(self, statuses):
        self.__statuses = {}
        for status in statuses:
            if status.column_name in self.__statuses:
                self.__statuses[status.column_name].append(status)
            else:
                self.__statuses[status.column_name] = [status]
    
    @property
    def items(self):
        return self.__statuses


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
