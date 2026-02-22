# Word = 'Hello'
#
# print(Word.istitle())

# def even_numbers(numbers = None):
#     numbers = list(numbers)
#     for i in numbers:
#         if i % 2 == 0:
#             yield i
#         else:
#             raise ValueError ("Error")
#
#
# print(list(even_numbers([2, 6])))

a = {1, 2, 3}
b = {3, 4, 5, 6}
print(a.union(b)) # - объединение
print(a.intersection(b)) # - пересечение

c = [1, 1, 2, 3, 4, 5, 6, 6, 6, 4]
print(set(c)) # - set удаляет повторяющиеся элементы
text = 'программирование'
print(set(text))



twizzy = ['Ivan', 'Maria', 'Ivan', 'Petr', 'Maria', 'Anna']
print(set(twizzy))


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = set(a) & set(b)

print(result)

only_in_a = set(a) - set(b)
print(only_in_a)

