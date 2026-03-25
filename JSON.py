import json

# settings = {
#     "user_id": 12345,
#     "theme": "dark",
#     "notifications": True
# }
#
# # Сохраняем словарь в файл
# with open('config.json', 'w') as f:
#     json.dump(settings, f, indent = 4) # indent делает файл красивым для человека
#
# # Читаем обратно в переменную (снова станет словарем)
# with open('config.json', 'r') as f:
#     loaded_settings = json.load(f)
#
# print(loaded_settings["theme"]) # Выведет: dark



data = {
    "name": "Ivan",
    "age": 25,
    "skills": ["Python", "Git"],
    "is_student": False
}

with open('config.json', 'w', encoding='utf-8') as p:
    json.dump(data, p, indent = 4)                      # json.dump нужен для того чтобы сохранять данные в файл. Как-бы "вывалить" данные в файл
                                                        # indent нужен для обозначения отступов, как бы для читабельности и красоты

with open('config.json', 'r', encoding = 'utf-8') as d:
    name = json.load(d)                                 # json.load нужен для того чтобы читать данные из файла. При чтении, Python обратно превращает словари в словари, а объекты - в объекты


print(name['skills'])
