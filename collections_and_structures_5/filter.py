names = ('Larissa', 'Rafael', 'Marcus', 'John')

def person_approved(person):
    if person == 'Marcus':
        return True
    else:
        return False

print(list(filter(person_approved, names)))
print(list(map(person_approved, names)))

paintings = [('Classic Painting', 'Paul', 1857),
            ('Medieval Painting', 'Red', 1867),
            ('Modern Painting', 'Green', 1897)]

def is_antique(painting):
    if painting[2] < 1890:
        return True
    else:
        return False

print(list(filter(is_antique, paintings)))
print(list(map(is_antique, paintings)))
