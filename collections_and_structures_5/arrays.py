# Arrays
from array import array

# Integers, decimal numbers and characters
numbers = array('i', [1, 2, 3, 4, 5, 6])

print(numbers)
numbers.append(10)

print(numbers)
numbers.insert(5, 200)

print(numbers)
numbers.pop(1)

print(numbers)
numbers.remove(5)

print(numbers)
del numbers[1]

print(numbers)
