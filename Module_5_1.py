class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует!")
        else:
            print(f"Вы приехали на {new_floor} этаж!")


new_house = House('ЖК Эльбрус', 30)

print(f'Дом: {new_house.name} \nЭтажей: {new_house.number_of_floors}')
move_floor = int(input("На какой этаж вы хотите переместиться? "))
new_house.go_to(move_floor)

