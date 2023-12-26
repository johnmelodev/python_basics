try:
    value = int(input('Enter a value in dollars: '))
    print(value * 5.25)
except:
    print('Please enter only numbers')

# More general exceptions, using index error

try:
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(months[15])
except IndexError as error:
    print('Please access a valid index')
    print(error)
