# Dictionary comprehension
# [expression for member in iterable]
# {key: expression for member in iterable}
from pprint import pprint

# Populating a dictionary with values
products = ['product1', 'product2', 'product3', 'product4', 'product5']
pprint({product: i for i, product in enumerate(products, 1)})

# Generating a test value matrix
# pprint({product: [0 for i in range(5)] for product in products})

# Generating a matrix of values multiplied by 2
pprint({product: [i * 2 for i in range(5)] for product in products})

pprint({product: [random.randint(1000, 15000)
       for i in range(5)] for product in products})
