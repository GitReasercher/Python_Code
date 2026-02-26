class Greeter:
    def __call__(self, name):
        self.name = name
        return f'Hello, I\'m {name}'

say_hi = Greeter()

print(say_hi('Colya'))

# tasks

#1

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f'The color of {self.brand} is {self.color}'

Toyota = Car('Toyota', 'red')
BMV = Car('BMV', 'blue')
Audi = Car('Audi', 'black')

print(BMV)

#2

class BankAccount:

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.blance = self.balance + amount

    def __str__(self):
        return f'The balance equalls {self.balance}'

my_account = BankAccount(5007.45)
print(my_account)



class Multiplier:
     def __init__(self, factor):
         self.factor = factor

     def __call__(self, value):
         return value * self.factor

# Создаем экземпляр (объект)
triple = Multiplier(3)

# Используем объект как функцию
print(triple(10))  # Выведет 30


class Math:

    def mul(self, x, y):
        self.x = x
        self.y = y
        return x * y

    def __call__(self, number):
        return self.x * self.y + number

counting = Math()

counting.mul(5, 6)
print(counting(1))


#3

class Counter:

    def addition(self, number):
        self.number = number
        return number

    def __call__(self):
        return self.number + 1

Addition = Counter()
Addition.addition(5)
print(Addition())



class Math:
    def multiply(self, number):
        self.number = number
        return number * self.number