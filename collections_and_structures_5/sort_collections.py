# Sort by property
from operator import itemgetter

people = [
    {'name': 'John', 'age': 31, 'access_level': 2},
    {'name': 'Carol', 'age': 23, 'access_level': 3},
    {'name': 'Thomas', 'age': 6, 'access_level': 1},
    {'name': 'Amanda', 'age': 36, 'access_level': 1}]

people.sort(key=itemgetter('access_level'))
print(people)

products = [('Cellphone', 750), ('Bicycle', 1500), ('Microphone', 550)]

products.sort(key=itemgetter(0))
print(products)

matrix = [[5, 10], [15, 21], [1, 13]]
matrix.sort(key=itemgetter(0))
print(matrix)


filming_equipment = [
    ('Tripod', 300),
    ('Camera', 1700),
    ('Lighting', 200),
]

filming_equipment.sort(key=itemgetter(1), reverse=True)
print(filming_equipment)


currency_quotes = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]
currency_quotes.sort(key=itemgetter(1))
print(currency_quotes)
