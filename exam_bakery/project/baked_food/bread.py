from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    __PORTION = 200

    def __init__(self, name, price):
        super().__init__(name, self.__PORTION, price)
