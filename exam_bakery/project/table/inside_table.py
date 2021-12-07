from project.table.table import Table


class InsideTable(Table):
    _INVALID_TABLE_NUMBER_MESSAGE = 'Inside table\'s number must be between 1 and 50 inclusive!'

    _MIN_TABLE_NUMBER = 1
    _MAX_TABLE_NUMBER = 50

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_type(self):
        return 'InsideTable'
