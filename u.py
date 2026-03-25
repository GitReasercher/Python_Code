stock = {
    'ноутбуки': 15,
    'мышки': 0,
    'клавиатуры': 8,
    'мониторы': 0,
    'коврики': 12,
    "флешки": 3
}

for stocks, value in stock.items():
    if value == 0:
        stock[stocks] = 10
        print(f'Товар {stocks} закуплен, теперь его 10 штук')
    else:
        print(f'Товар {stocks} в наличии: {value} штук')

# 2 случай, когда обязательно надор использовать list()

for stocks, value in list(stock.items()):
    if value == 0:
        del stock[stocks]
        print(f'Удалён товар {stock}')

print("\nИтоговый склад после удаления пустых позиций:")
print(stock)


# Используем list(), так как будем СОЗДАВАТЬ новые ключи внутри цикла
for stocks, value in list(stock.items()):
    if value > 10:
        # Создаем имя для нового ключа
        new_item_name = f"Акция на {stocks}"

        # ДОБАВЛЯЕМ новый элемент в словарь
        stock[new_item_name] = "Скидка 10%"

        print(f"Система создала новую позицию: {new_item_name}")

print("\n--- Итоговый склад с акциями ---")
print(stock)
