class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors == other
        else:
            raise ValueError("Операция невозможна. Атрибут other должен быть типом int, float или объектом House")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors < other
        else:
            raise ValueError("Операция невозможна. Атрибут other должен быть типом int, float или объектом House")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors <= other
        else:
            raise ValueError("Операция невозможна. Атрибут other должен быть типом int, float или объектом House")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors > other
        else:
            raise ValueError("Операция невозможна. Атрибут other должен быть типом int, float или объектом House")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors >= other
        else:
            raise ValueError("Операция невозможна. Атрибут other должен быть типом int, float или объектом House")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors != other
        else:
            raise ValueError("Операция невозможна. Атрибут other должен быть типом int, float или объектом House")

    def __add__(self, value):
        if isinstance(value, (int, float, House)):
            self.number_of_floors += value
            return self
        else:
            raise ValueError("Операция невозможна. Атрибут value должен быть типом int, float или объектом House")

    def __iadd__(self, value):
        if isinstance(value, (int, float, House)):
            return self + value
        else:
            raise ValueError("Операция невозможна. Атрибут value должен быть типом int, float или объектом House")

    def __radd__(self, value):
        if isinstance(value, (int, float, House)):
            return self + value
        else:
            raise ValueError("Операция невозможна. Атрибут value должен быть типом int, float или объектом House")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
