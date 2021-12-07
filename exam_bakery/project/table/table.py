from abc import ABC, abstractmethod

from project.utils import is_positive


class Table(ABC):
    __INCORRECT_CAPACITY_MESSAGE = 'Capacity has to be greater than 0!'
    _INVALID_TABLE_NUMBER_MESSAGE = None

    _MIN_TABLE_NUMBER = None
    _MAX_TABLE_NUMBER = None

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = list()
        self.drink_orders = list()
        self.number_of_people = 0
        self.is_reserved = False
        self.initialize()

    def initialize(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    @classmethod
    def __validate_capacity(cls, value):
        if not is_positive(value):
            raise ValueError(cls.__INCORRECT_CAPACITY_MESSAGE)

    @classmethod
    def __validate_table_number(cls, value):
        if cls._MIN_TABLE_NUMBER and cls._MIN_TABLE_NUMBER > value:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)
        if cls._MAX_TABLE_NUMBER and cls._MAX_TABLE_NUMBER < value:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.initialize()

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.table_type}\n" \
                   f"Capacity: {self.capacity}"
        return None

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self.__capacity = value

    @property
    @abstractmethod
    def table_type(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self.__table_number = value
