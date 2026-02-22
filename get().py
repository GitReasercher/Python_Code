# numbers = {'number': 3}
#
# try:
#     print(numbers.get('number'))
# except ValueError:
#     pass

settings = {
    "theme": "dark",
    "font_size": 14,
    "language": "ru",
}
print(settings.items())
print(settings.values())

notifications = settings.get('notification:', 'По умолчани.: вкл.')

theme = settings.get('theme:', 'По умолчанию: light')

print(settings.get('theme'))

for val in settings:
    print(f'Значения настроек {val}')