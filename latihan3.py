class lion:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} mengaum")

my_lion = lion("candra")

my_lion.bark()

class Animal:
     def speak(self):
         print("Hewan berbicara.")

class cat(Animal):
    def bark(self):
        print("kucing mengeong.")

cat = cat()

cat.speak()
cat.bark()

class Animal:
    def speak(self):
        return "Hewan berbicara."

class Dog(Animal):
    def speak(self):
        return "Anjing menggonggong!"

dog = Dog()

print(dog.speak())

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(200)

account.deposit(430)

print(account.get_balance())

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Anjing menggonggong!"

dog = Dog()

print(dog.speak())

class Cat(Animal):

    def speak(self):
        return "Kucing mengeong!"

cat = Cat()

print(cat.speak())