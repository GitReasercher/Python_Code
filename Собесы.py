def list_numbers(numbers):
    unique = set(numbers)
    return unique

print(list_numbers([1, 2, 2, 3, 4, 4, 4, 5]))


for i in range(1, 100):
    if i % 3 == 0:
        print('Fizz')

    elif i % 5 == 0:
        print('Buzz')

    else:
        print('FizzBuzz')



