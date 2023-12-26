# Functions
# input()
# len()
# split()

def welcome():
    print('Welcome!')


welcome()


def personalized_welcome(name, age, Last):
    print(f'Welcome {name}!')


personalized_welcome('Joao', 25, 'Melo')


def introduce_place(operating_hours, place='our store'):
    print(
        f'Get to know {place}, operating hours from {operating_hours}')


# if you leave the place empty it is filled by the default value our store. if you fill something like the example below disney it fills in a personalized way
introduce_place('08:00 to 18:00', 'Disney')


def generate_full_name(person_name):
    print(f'Welcome! {person_name}')


generate_full_name('Sam')


def calculate_values(product_price, quantity=1):
    print(product_price * quantity)


calculate_values(25, 3)
