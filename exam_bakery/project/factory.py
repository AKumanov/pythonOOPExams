from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Factory:
    def __init__(self):
        pass

    @staticmethod
    def create_food_by_type(food_type: str, name: str, price: float):
        if food_type == Bread.__name__:
            return Bread(name, price)
        if food_type == Cake.__name__:
            return Cake(name, price)
        return None

    @staticmethod
    def create_drink_by_type(drink_type: str, name: str, portion: float, brand: str):
        if drink_type == Tea.__name__:
            return Tea(name, portion, brand)
        if drink_type == Water.__name__:
            return Water(name, portion, brand)
        return None

    @staticmethod
    def create_table_by_type(table_type, table_number, capacity):
        if table_type == InsideTable.__name__:
            return InsideTable(table_number, capacity)
        if table_type == OutsideTable.__name__:
            return OutsideTable(table_number, capacity)
        return None
