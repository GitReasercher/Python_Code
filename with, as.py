with open('Test.txt', 'w', encoding='utf-8') as f: # Работаем с файлом через перемнную f
    f.write('Hello World!')
    lines = ['\nUSA,', " Russia"]
    f.writelines(lines)

# Если есть список, можно использовать writelines


