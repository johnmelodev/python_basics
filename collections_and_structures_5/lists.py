# Create lists
# Method 1

numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

# or using map function
names = ['Larissa', 'Rafael', 'Marcus', 'John']


def approve_person(name):
    return name + ' Approved'


print(list(map(approve_person, names)))
