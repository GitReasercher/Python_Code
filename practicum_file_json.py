import json
#
# user = {
#     'name': 'Ivan',
#     'age': 36,
#     'language': 'Russian'
# }
#
# with open('profile.json', 'w', encoding = 'utf-8') as pr:
#     json.dump(user, pr, ensure_ascii=False, indent = 4)


# list_1 = ["Купить хлеб", "Выучить Python"]
#
# with open('profile.json', 'r', encoding='utf-8') as check:
#     data = json.load(check)
#     print(data)
#
# list_1.append('Покормить кота')
#
# with open('profile.json', 'w', encoding='utf-8') as check:
#     json.dump(list_1, check, ensure_ascii=False, indent=4)

list_2 = [
    {"name": "Аня", "balance": 500},
    {"name": "Боря", "balance": 1200},
    {"name": "Витя", "balance": 300},
    {"name": "Дима", "balance": 2500}
]

with open('bank.json', 'w', encoding='utf-8') as bank_json:
    json.dump(list_2, bank_json, indent=4, ensure_ascii=False)


with open('bank.json', 'r', encoding = 'utf-8') as bank_json:
    d = json.load(bank_json)
    for user in d:
        if user['balance'] > 1000:
            print(user['name'])


