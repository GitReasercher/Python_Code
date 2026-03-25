import sys

password = input('Enter ur password: ')

if password != '1234':
    print('Wrong password')
    sys.exit(222222) # - в exit() указывается код ошибки или пишетя текстом
else:
    print('Login successful')