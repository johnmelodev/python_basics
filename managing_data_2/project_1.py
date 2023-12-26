# Module 1
from datetime import datetime
import random

print('   Hello, welcome to our company   ')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
registration_date = datetime.now()
cards = ['$50.00', '$250.00', '$120.00']
card = random.choice(cards)
birthday = datetime.strptime(
    input('Enter your birthday in the format dd/mm/yyyy: '), '%d/%m/%Y')

# Module
print(f'Hello {name}, your registration was successfully completed on {registration_date.day}/{registration_date.month}/{
      registration_date.year}\nCongratulations, there was a draw and you won a shopping card worth {card}')
