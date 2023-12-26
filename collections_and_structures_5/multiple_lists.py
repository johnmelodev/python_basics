# working with multiple lists
from itertools import zip_longest

a_list = ['A', 'B', 'C', 'D', 'E']
b_list = [1, 2, 3, 4, 6]

for a, b in zip(a_list, b_list):
    print(a)
    print(b)

products = ['product 1', 'product 2', 'product 3', 'product 4', 'product 5']
prices = [250, 150, 220, 550, 50]

for a, b in zip(products, prices):
    print(f'Saving product {a} value R$ {b}')

titles = ['Title 1', 'Title 2', 'Title 3', 'Title 4']
descriptions = ['Description 1', 'Description 2', 'Description 3']

for title, description in zip_longest(titles, descriptions):
    print(f'We found the {title} description: {description}')


products = ['product 1', 'product 2', 'product 3', 'product 4', 'product 5']
prices = ['500,00', '1500,00', '2700,00', '5000,00']

for product, price in zip_longest(products, prices):
    print(f'{product} found at the price of R${price}')
