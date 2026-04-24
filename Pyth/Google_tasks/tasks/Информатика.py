# 1 Задача

import random

number = random.randint(100, 999)

print(number)

number_1_1 = number % 100
number_1 = number_1_1 % 10 # еденицы
number_2 = number_1_1 // 10 # десятки
number_3 = number // 100 # сотни

print(f'Сотен: {number_3}\n Десятков: {number_2}\n Единиц: {number_1}')


# 2 Задача

Age_of_Anton = int(input('Возраст антона: ')) 
Age_of_Boris = int(input('Возраст бориса: '))
Age_of_Victor = int(input('Возраст виктора:'))

if Age_of_Boris < Age_of_Victor:
    if Age_of_Anton < Age_of_Victor:
        print(f'Возраст Бориса = {Age_of_Boris};\n Возраст Антона = {Age_of_Anton};\n Возраст Виктора = {Age_of_Victor}\n - Виктор старший')
else:
    if Age_of_Victor < Age_of_Boris:
        if Age_of_Boris > Age_of_Anton:
            print(f'Возраст Бориса = {Age_of_Boris};\n Возраст Антона = {Age_of_Anton};\n Возраст Виктора = {Age_of_Victor}\n - Борис старший')

if Age_of_Boris < Age_of_Anton:
    if Age_of_Anton > Age_of_Victor:
        print(f'Возраст Бориса = {Age_of_Boris};\n Возраст Антона = {Age_of_Anton};\n Возраст Виктора = {Age_of_Victor}\n - Антон старший')