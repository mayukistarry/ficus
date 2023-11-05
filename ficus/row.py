class RowInterface:
    def __init__(self):
        pass
    
    @property
    def value(self):
        raise Exception('Not implemented')
    
    @property
    def column_name(self):
        raise Exception('Not implemented')