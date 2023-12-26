# Enumerate
for index, number in enumerate(range(1, 11), 1):
    print(index, number)
    if index == 5:
        print('We are halfway through the list')

names = ['name1', 'name2', 'name3', 'name4', 'name5']

for index, name in enumerate(names, 1):
    print(index, name)
    if index == 3:
        print('We have 3 people registered')


fruit = ['Apple', 'Orange', 'Strawberry', 'Lemon']

for index, fruit in enumerate(fruit, 0):
    if index == 3:
        print(f'{index}, {fruit} on sale')
    else:
        print(index, fruit)
