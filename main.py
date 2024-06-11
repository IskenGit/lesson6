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
    def make_sound(self):
        pass
    def eat(self):
        pass
class Bird(Animal):
    def __init__(self):
        super().__init__(name,age)
        name = bird
        age = 5
        print(f'{name} обычно живет {age} лет')
    def make_sound(self):
        print("Чик чирик")
    def eat(self):
        print("кушает траву, червей и рыб")
class Mammal(Animal):
    def __init__(self):
        super().__init__(name,age)
        name = mammal
        age = 10
        print(f'{name} обычно живет {age} лет')
    def make_sound(self):
        print("млям")
    def eat(self):
        print("питается в основном молоком")
class Reptile(Animal):
    def __init__(self):
        super().__init__(name,age)
        name = reptile
        age = 35
        print(f'{name} обычно живет {age} лет')
    def make_sound(self):
        print("тптсссс")
    def eat(self):
        print("питается в основном насекомыми")
animals = [Bird(),Mammal(),Reptile()]
for animal in animals:
    animal.make_sound()
    animal.eat()
