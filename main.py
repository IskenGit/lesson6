# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'{name} обычно живет {age} лет')
    def make_sound(self):
        pass
    def eat(self):
        pass
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
    def make_sound(self):
        print(f'{self.name} создает звук "Чик чирик"')
    def eat(self):
        print("кушает траву, червей и рыб")
class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print(f'{self.name} создает звук "млям"')
    def eat(self):
        print("питается в основном молоком")
class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print(f'{self.name} создает звук "тптсссс"')
    def eat(self):
        print("питается в основном насекомыми")
# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
animals = [
    Bird(name="Воробей", age=3),
    Mammal(name="Коала", age=12),
    Reptile(name="Ящерица", age=5)
]
for animal in animals:
    animal.make_sound()
    animal.eat()
print("\nДемонстрация полиморфизма:")
animal_sound(animals)