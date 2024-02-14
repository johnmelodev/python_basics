# How to use a list comprehension
# new_list = [2 * i for i in range(10)]

# [expression for member in iterable]
# print(new_list)

# Example with a list of names

'''
names = ['Larissa', 'rafael', 'marcus', 'john']
print([name + ' APPROVED' for name in names])
print([approve_person(name) for name in names])
'''


from pprint import pprint
pprint([[i for i in range(1, 6)] for x in range(5)])


def approve_person(name):
    return name + ' APPROVED'


# Using conditionals in list comprehension
# [expression for member in iterable (conditional if)]
names = ['Larissa', 'Rafael', 'Marcus', 'John']
print([approve_person(name) for name in names if name != 'rafael'])

# Numeric values
print([i for i in range(20) if i not in (1, 5, 15, 19)])

#################

def even_number(number):
    value = number % 2
    if value == 0:
        return True
    else:
        return False

print([i for i in range(20) if even_number(i)])

##################################
# Using list comprehension to create a list of even numbers
# The conditional is flexible
# [expression (conditional if) for member in iterable]
participants = ['Larissa', 'rafael', 'marcus', 'john']
winners = ['marcus', 'john']
print([i + ' WINNER' if i in winners else i + ' NOT SELECTED' for i in participants])
