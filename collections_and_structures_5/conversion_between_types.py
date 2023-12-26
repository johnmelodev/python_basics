# Conversion between types
age = input('Enter your age: ')
print(int(age) > 17)

year_of_publication = 2020
print('This book was created in ' + str(year_of_publication))

height = input('Height of the wall? ')
print(float(height) > 2.50)

# conversions between collections
greeting = 'Hello'
print(list(greeting))
print(set(greeting))
print(tuple(greeting))
print(list(range(30)))


numbers = [10, 20, 20, 50]
print(set(numbers))
print(tuple(numbers))
print(type(numbers))