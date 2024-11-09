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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name} \nКоличество этажей: {self.number_of_floors}'


new_house = House('ЖК Эльбрус', 30)
new_house2 = House('ЖК Акация', 20)

print(new_house.__str__())
print(new_house.__len__())

print(new_house2.__str__())
print(new_house2.__len__())
