"""
Демонстрация работы методов базового и производных классов.
Программа показывает принципы ООП: наследование, полиморфизм, инкапсуляцию.
"""

from abc import ABC, abstractmethod
from typing import List

# Абстрактный базовый класс
class Animal(ABC):
    def __init__(self, name: str, age: int):
        self._name = name  # Инкапсуляция: защищенный атрибут
        self._age = age
        self._health = 100
    
    @property
    def name(self) -> str:
        """Геттер для имени (инкапсуляция)"""
        return self._name
    
    @property
    def age(self) -> int:
        """Геттер для возраста"""
        return self._age
    
    @property
    def health(self) -> int:
        """Геттер для здоровья"""
        return self._health
    
    @abstractmethod
    def make_sound(self) -> str:
        """Абстрактный метод - должен быть реализован в дочерних классах"""
        pass
    
    def move(self) -> str:
        """Общий метод для всех животных"""
        return f"{self._name} передвигается"
    
    def eat(self, food: str) -> str:
        """Общий метод для всех животных"""
        return f"{self._name} ест {food}"
    
    def __str__(self) -> str:
        """Строковое представление объекта"""
        return f"{self.__class__.__name__} {self._name}, возраст: {self._age}, здоровье: {self._health}"

# Производный класс - Собака
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self._breed = breed  # Уникальный атрибут для собак
        self._tricks = []    # Список изученных команд
    
    @property
    def breed(self) -> str:
        """Геттер для породы"""
        return self._breed
    
    def make_sound(self) -> str:
        """Переопределение абстрактного метода"""
        return f"{self._name} лает: Гав-гав!"
    
    def learn_trick(self, trick: str) -> str:
        """Уникальный метод для собак"""
        if trick not in self._tricks:
            self._tricks.append(trick)
            return f"{self._name} выучил новую команду: {trick}"
        return f"{self._name} уже знает команду {trick}"
    
    def perform_trick(self, trick: str) -> str:
        """Уникальный метод для собак"""
        if trick in self._tricks:
            return f"{self._name} выполняет команду: {trick}"
        return f"{self._name} не знает команду {trick}"
    
    def get_tricks(self) -> List[str]:
        """Возвращает список изученных команд"""
        return self._tricks.copy()  # Возвращаем копию для инкапсуляции

# Производный класс - Кошка
class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self._color = color  # Уникальный атрибут для кошек
        self._lives = 9      # Уникальный атрибут
    
    @property
    def color(self) -> str:
        """Геттер для цвета"""
        return self._color
    
    @property
    def lives(self) -> int:
        """Геттер для количества жизней"""
        return self._lives
    
    def make_sound(self) -> str:
        """Переопределение абстрактного метода"""
        return f"{self._name} мяукает: Мяу-мяу!"
    
    def purr(self) -> str:
        """Уникальный метод для кошек"""
        return f"{self._name} мурлычет: Мрррр..."
    
    def lose_life(self) -> str:
        """Уникальный метод для кошек"""
        if self._lives > 1:
            self._lives -= 1
            return f"{self._name} потерял жизнь. Осталось жизней: {self._lives}"
        return f"{self._name} использовал все жизни!"

# Производный класс - Птица
class Bird(Animal):
    def __init__(self, name: str, age: int, wingspan: float):
        super().__init__(name, age)
        self._wingspan = wingspan  # Уникальный атрибут
        self._can_fly = True
    
    @property
    def wingspan(self) -> float:
        """Геттер для размаха крыльев"""
        return self._wingspan
    
    def make_sound(self) -> str:
        """Переопределение абстрактного метода"""
        return f"{self._name} поет: Чик-чирик!"
    
    def fly(self) -> str:
        """Уникальный метод для птиц"""
        if self._can_fly:
            return f"{self._name} летает"
        return f"{self._name} не может летать"
    
    def set_fly_ability(self, can_fly: bool) -> None:
        """Изменение способности к полету"""
        self._can_fly = can_fly

# Фабрика для создания животных
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        """Фабричный метод для создания животных"""
        if animal_type.lower() == "dog":
            return Dog(*args)
        elif animal_type.lower() == "cat":
            return Cat(*args)
        elif animal_type.lower() == "bird":
            return Bird(*args)
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

# Основная тестовая программа
def demonstrate_oop_principles():
    """Демонстрация принципов ООП"""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ МЕТОДОВ БАЗОВОГО И ПРОИЗВОДНЫХ КЛАССОВ")
    print("=" * 60)
    
    # Создание объектов через фабрику
    try:
        animals = [
            AnimalFactory.create_animal("dog", "Барсик", 3, "овчарка"),
            AnimalFactory.create_animal("cat", "Мурка", 2, "рыжий"),
            AnimalFactory.create_animal("bird", "Кеша", 1, 0.5)
        ]
    except ValueError as e:
        print(f"Ошибка создания животных: {e}")
        return
    
    # 1. Демонстрация наследования и полиморфизма
    print("\n1. НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ:")
    print("-" * 40)
    
    for animal in animals:
        # Вызов переопределенных методов
        print(f"{animal.name}: {animal.make_sound()}")
        # Вызов унаследованных методов
        print(f"{animal.move()}")
        print(f"{animal.eat('корм')}")
        print()
    
    # 2. Демонстрация уникальных методов
    print("\n2. УНИКАЛЬНЫЕ МЕТОДЫ:")
    print("-" * 40)
    
    for animal in animals:
        if isinstance(animal, Dog):
            print(animal.learn_trick("сидеть"))
            print(animal.perform_trick("сидеть"))
            print(f"Порода: {animal.breed}")
            
        elif isinstance(animal, Cat):
            print(animal.purr())
            print(animal.lose_life())
            print(f"Цвет: {animal.color}")
            
        elif isinstance(animal, Bird):
            print(animal.fly())
            print(f"Размах крыльев: {animal.wingspan}м")
        
        print()
    
    # 3. Демонстрация инкапсуляции
    print("\n3. ИНКАПСУЛЯЦИЯ:")
    print("-" * 40)
    
    dog = animals[0]
    print(f"Имя через геттер: {dog.name}")
    print(f"Возраст через геттер: {dog.age}")
    print(f"Здоровье через геттер: {dog.health}")
    
    # Попытка прямого доступа к защищенным атрибутам (вызовет ошибку)
    try:
        # print(dog._name)  # Так делать не рекомендуется, но технически возможно
        pass
    except AttributeError:
        print("Прямой доступ к защищенным атрибутам невозможен")
    
    # 4. Демонстрация работы с коллекциями объектов
    print("\n4. РАБОТА С КОЛЛЕКЦИЯМИ ОБЪЕКТОВ:")
    print("-" * 40)
    
    # Создание зоопарка
    zoo = [
        Dog("Рекс", 5, "доберман"),
        Cat("Васька", 4, "черный"),
        Bird("Гоша", 2, 0.7),
        Dog("Шарик", 2, "дворняжка")
    ]
    
    print("Все обитатели зоопарка:")
    for i, animal in enumerate(zoo, 1):
        print(f"{i}. {animal}")
    
    # Группировка по типам
    dogs = [animal for animal in zoo if isinstance(animal, Dog)]
    cats = [animal for animal in zoo if isinstance(animal, Cat)]
    birds = [animal for animal in zoo if isinstance(animal, Bird)]
    
    print(f"\nСобак в зоопарке: {len(dogs)}")
    print(f"Кошек в зоопарке: {len(cats)}")
    print(f"Птиц в зоопарке: {len(birds)}")
    
    # 5. Демонстрация обработки ошибок
    print("\n5. ОБРАБОТКА ОШИБОК:")
    print("-" * 40)
    
    try:
        unknown_animal = AnimalFactory.create_animal("fish", "Немо", 1)
    except ValueError as e:
        print(f"Поймана ошибка: {e}")
    
    # 6. Демонстрация полиморфизма в действии
    print("\n6. ПОЛИМОРФИЗМ В ДЕЙСТВИИ:")
    print("-" * 40)
    
    def animal_concert(animals_list: List[Animal]):
        """Функция, демонстрирующая полиморфизм"""
        for animal in animals_list:
            print(animal.make_sound())
    
    animal_concert(zoo)

# Дополнительные тесты
def run_additional_tests():
    """Дополнительные тесты для демонстрации"""
    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ")
    print("=" * 60)
    
    # Тест наследования
    dog = Dog("Бобик", 4, "лабрадор")
    print(f"Тест наследования: {isinstance(dog, Animal)}")  # True
    
    # Тест уникальных методов
    print(dog.learn_trick("лежать"))
    print(dog.perform_trick("лежать"))
    
    # Тест инкапсуляции
    print(f"Имя: {dog.name}")  # Работает через геттер
    
    # Тест абстрактного класса
    try:
        # animal = Animal("Абстракт", 1)  # Вызовет ошибку
        pass
    except TypeError as e:
        print(f"Нельзя создать экземпляр абстрактного класса: {e}")

if __name__ == "__main__":
    demonstrate_oop_principles()
    run_additional_tests()
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!")
    print("=" * 60)

if __name__ == "__main__":
    main()
