class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'title of the book is {self.title}, author is {self.author}, pages is {self.pages}.'

    def __len__(self):
        return self.pages

my_book = Book('The sea', 'Asad', 245)

print(my_book)


class Hero:

    def __init__(self, health, weapon, age):
        self.health = health
        self.weapon = weapon
        self.age = age

    def __str__(self):
        return f'health of the Hero: {self.health}; weapon of the Hero: {self.weapon}; age of the Hero: {self.age}'

hero = Hero(3000, 'sword', 24)
print(hero)