from project.factory import Factory
from project.utils import check_string_empty_or_white_space


class Bakery:
    __INVALID_NAME_MESSAGE = 'Name cannot be empty string or white space!'

    def __init__(self, name):
        self.name = name
        self.food_menu = list()
        self.drinks_menu = list()
        self.tables_repository = list()
        self.total_income = 0

    @classmethod
    def __validate_name(cls, value):
        if not check_string_empty_or_white_space(value):
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    def __find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return True
        return False

    def __find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return True
        return False

    def __find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return True
        return False

    def __get_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def __get_food_by_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food
        return None

    def __get_drink_by_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink
        return None

    def __find_available_table_for_people(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                return table
        return None

    def add_food(self, food_type: str, name: str, price: float):
        if self.__find_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = Factory().create_food_by_type(food_type, name, price)
        if food:
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if self.__find_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = Factory().create_drink_by_type(drink_type, name, portion, brand)
        if drink:
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.__find_table_by_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = Factory().create_table_by_type(table_type, table_number, capacity)
        if table:
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__find_available_table_for_people(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_name):
        food_name_data = list(food_name)
        ordered_food = list()
        unordered_food = list()
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        for current_food_name in food_name_data:
            food = self.__get_food_by_name(current_food_name)
            if food:
                ordered_food.append(str(food))
                table.order_food(food)
            else:
                unordered_food.append(current_food_name)
        output = f"Table {table_number} ordered:\n"
        output += '\n'.join(ordered_food)
        output += '\n'
        output += f'{self.name} does not have in the menu:\n'
        output += '\n'.join(unordered_food)
        return output.strip()

    def order_drink(self, table_number: int, *drinks_name):
        drink_name_data = list(drinks_name)
        ordered_drink = list()
        unordered_drink = list()
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        for current_drink_name in drink_name_data:
            drink = self.__get_drink_by_name(current_drink_name)
            if drink:
                ordered_drink.append(str(drink))
                table.order_drink(drink)
            else:
                unordered_drink.append(current_drink_name)
        output = f"Table {table_number} ordered:\n"
        output += '\n'.join(ordered_drink)
        output += '\n'
        output += f'{self.name} does not have in the menu:\n'
        output += '\n'.join(unordered_drink)
        return output.strip()

    def leave_table(self, table_number: int):
        table = self.__get_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table.table_number}\n" \
                   f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        output = []
        for table in self.tables_repository:
            if not table.is_reserved:
                output.append(table.free_table_info())
        return '\n'.join(output)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

# b = Bakery('Test')
# print(b.add_table('InsideTable', 10, 5))
# print(b.add_table('OutsideTable', 51, 7))
# print(b.add_drink('Water', 'Mineral', 100, 'Bankya'))
# print(b.add_drink('Water', 'Tap Water', 100, 'Devnya'))
# print(b.add_drink('Water', 'Blue', 100, 'Mihaelovo'))
# print(b.order_drink(10, 'Mineral', 'Tap Water', 'Blue', 'Test'))
# print(b.add_food("Cake", 'Lemon', 1.50))
# print(b.add_food("Cake", 'Cherry', 1.50))
# print(b.add_food("Cake", 'Banana', 1.50))
# print(b.add_food("Cake", 'Strawberry', 1.50))
# print(b.order_food(10, 'Lemon', 'Cherrry', 'Banana', 'Strawberry'))
# print(b.leave_table(10))
# print(b.get_free_tables_info())
# print(b.get_total_income())
