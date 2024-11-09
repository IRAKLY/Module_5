class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if self.number_of_floors >= new_floor >= 1:
            for new_floor in range(1, new_floor + 1):
                print(f"Вы приехали на {new_floor} этаж!")
        else:
            print("Такого этажа не существует!")


new_house = House('ЖК Эльбрус', 30)

print(f'Дом: {new_house.name} \nЭтажей: {new_house.number_of_floors}')
move_floor = int(input("На какой этаж вы хотите переместиться? "))
new_house.go_to(move_floor)

