def display_price(product_name, price):
    print(f'{product_name} is priced at: {price}')


# Named arguments
display_price(price=5000, product_name='iPhone')

# Positional arguments


def get_custom_object(height, shape):
    print(height, shape)


get_custom_object(1.5, 'square')

# Named and positional arguments


def generate_custom_object(color, height, shape):
    print(color, height, shape)


generate_custom_object('Blue', height=2.10, shape='Square')
