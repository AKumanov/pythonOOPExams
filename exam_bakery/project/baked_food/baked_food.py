from abc import ABC, abstractmethod

from project.utils import check_string_empty_or_white_space


class BakedFood(ABC):
    __INVALID_NAME_MESSAGE = 'Name cannot be empty string or white space!'
    __INVALID_PRICE_MESSAGE = 'Price cannot be less than or equal to zero!'

    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @classmethod
    def __validate_name(cls, value):
        if not check_string_empty_or_white_space(value):
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_price(cls, value):
        if value <= 0:
            raise ValueError(cls.__INVALID_PRICE_MESSAGE)

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value
