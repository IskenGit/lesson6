import pickle

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age} лет"

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.position}"

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} кормит {animal.name}.")
        else:
            raise ValueError("Объект не является экземпляром класса Animal")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} лечит {animal.name}.")
        else:
            raise ValueError("Объект не является экземпляром класса Animal")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Объект не является экземпляром класса Animal")

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise ValueError("Объект не является экземпляром класса Employee")

    def show_animals(self):
        if self.animals:
            print("Животные в зоопарке:")
            for animal in self.animals:
                print(animal)
        else:
            print("В зоопарке нет животных")

    def show_employees(self):
        if self.employees:
            print("Сотрудники зоопарка:")
            for employee in self.employees:
                print(employee)
        else:
            print("В зоопарке нет сотрудников")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Информация о зоопарке сохранена в файл {filename}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
            print(f"Информация о зоопарке загружена из файла {filename}")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создан новый зоопарк.")
            return Zoo("Новый зоопарк")

# Пример использования
filename = 'zoo_data.pkl'

# Попробуем загрузить зоопарк из файла, если файл существует
zoo = Zoo.load_from_file(filename)

# Добавляем животных и сотрудников, если зоопарк пустой (новый)
if not zoo.animals:
    zoo.add_animal(Animal("Лев", "Пантеровые", 5))
    zoo.add_animal(Animal("Жираф", "Жирафовые", 8))

if not zoo.employees:
    zoo.add_employee(ZooKeeper("Иван Иванов"))
    zoo.add_employee(Veterinarian("Мария Петрова"))

# Выводим список животных и сотрудников
zoo.show_animals()
zoo.show_employees()

# Применяем специфические методы сотрудников
keeper = zoo.employees[0]  # Иван Иванов
vet = zoo.employees[1]  # Мария Петрова

keeper.feed_animal(zoo.animals[0])  # Иван Иванов кормит Лев.
vet.heal_animal(zoo.animals[1])  # Мария Петрова лечит Жираф.

# Сохраняем зоопарк в файл перед выходом
zoo.save_to_file(filename)
