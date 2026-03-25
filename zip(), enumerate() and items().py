names = ['Vanya', 'Olya', 'Nastya']

salary = [1000000, 1000000, 1000000]

for name, salary in zip(names, salary):
    print(f'{name} has {salary} dollars')


players = [
    'Vanya', 'Olya', 'Nastya'
]

for place, players in enumerate(players, start = 1):
    print(f'player {players} won at {place} place')


server_status = {
    "CPU": "45%",
    "RAM": "2.4GB",
    "Status": "Online"
}

# Используем .items(), чтобы получить и ключ (key), и значение (value)
for parameter, value in server_status.items():
    print(f"Показатель {parameter} сейчас равен {value}")

