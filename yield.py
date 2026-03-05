def count(my_list):
    for item in my_list:
        yield item

my_list = [1, 2, 3, 4, 5]

generator = count(my_list)
#print(next(generator))
#print(next(generator))
#print(next(generator))
#print(next(generator))
#print(next(generator))
#print(next(generator))



def clean_conveyor(bottles):
    for bottle in bottles:
        if bottle >= 100:
            yield bottle
        elif bottle == 0:
            pass
        else:
            pass


production_line = [150, 50, 200, 0, 300]

for bottle in clean_conveyor(production_line):
    print(f'Bottle {bottle} ml')


def custom_range(start, step):
    while True:
        yield start
        start += step

for i in custom_range(1, 5):
    if i > 20:
        break
    else:
        print(i)



def filter_logs(lines, keyword):
    for line in lines:

        if keyword in line:
            yield line

logs = {
    "INFO": "Server started",
    'ERROR': 'Connection failed'
}

for i in filter_logs(logs, 'ERROR'):
    print(f'Найдена запись {i}')