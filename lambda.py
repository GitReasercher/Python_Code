names1 = ["Александр", "Яна", "Игорь"]

names1.sort(key=lambda name: len(name))

#print(names)

square = lambda x: x * x
print(square(4))



Hello = lambda name: f'Hello {name}'

print(Hello('fff'))