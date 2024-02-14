# How can we create lists?
# Create lists using Loops and Range()
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

# Map
names = ['Larissa', 'Rafael', 'Marcus', 'John']


def approve_person(name):
    return name + ' APPROVED'


print(list(map(approve_person, names)))
