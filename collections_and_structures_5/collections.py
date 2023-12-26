price_1 = 30
price_2 = 20
price_3 = 10

# Lists
prices = [10, 20, 30, 50, 100, 250, 500, 23, 63, 74]
print(prices[0])  # index
print(prices[prices.index(100)])

items = [1, 3, 6, 'Hello', 'Coffee', True, 10.6]
print(items[4])

# Different ways to generate a list
# Multiplication of values (repetition)
list_of_nines = [9] * 10
list_of_tests = ['Test'] * 10

print(list_of_nines)
print(list_of_tests)

# Using Range generator (Sequence)
# 1 to 29
range_of_numbers = list(range(30))
print(range_of_numbers)

# Generate from strings
print(list('Welcome to the training'))

# List of lists (matrix)
matrix_of_names = [['Carol', 30], ['Marcus', 50]]
print(matrix_of_names[0])
print(matrix_of_names[0][0])
print(matrix_of_names[1][0])


objects = ('cup', 'comb', 'cellphone')
print(objects)

range_of_numbers2 = list(range(10, 131))
print(range_of_numbers2)

print(list(objects) + range_of_numbers2)
