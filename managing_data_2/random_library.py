# random values with random
import random

print(random.random())  # Generates a value from 0.0 to 1.0
# Generates a decimal value from minimum value to maximum value

print(random.uniform(4, 10))  # Generates a value from 0.0 to 1.0
# Generates a decimal value from minimum value to maximum value

print(random.randint(1, 1000000))

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
print(random.choice(notes))

# or more than one random within the list

print(random.choices(notes, k=2))

cards_of_a_deck = ['card1', 'card2',
                   'card3', 'card4']  # shuffle a list
print(random.shuffle(cards_of_a_deck))
print(cards_of_a_deck)

results = ['head', 'tail']
print(random.choices(results))

names = ['kleber', 'claudia',
         'maristela', 'juliana']
print(random.choices(names))

print(random.randint(10, 100))
