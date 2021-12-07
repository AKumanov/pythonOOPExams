from project.drink.drink import Drink


class Water(Drink):
    __PRICE = 1.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.__PRICE, brand)
