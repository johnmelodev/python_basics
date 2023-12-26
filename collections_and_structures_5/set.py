numbers = {2, 2, 5, 8}
fruits = {'apple', 'grape', 'banana', 'apple', 'strawberry'}

set_numbers = set(numbers)
set_fruits = set(fruits)

print(set_numbers)
print(set_fruits)

# Adding new values
set_numbers.add(10)
print(set_fruits)

# Sets
numbers1 = [2, 2, 5, 8]
numbers2 = [2, 2, 3, 9]

a = set(numbers1)
b = set(numbers2)
print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))
