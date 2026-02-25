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