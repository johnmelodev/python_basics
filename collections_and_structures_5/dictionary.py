# Dictionaries
'''
Person
    name
    age
    height
'''

person = ['Carol', 18, 1.60, 'Mike', 50, 1.80]

# or to organize better
dictionary_person = {'name': 'Carol', 'age': 18, 'height': 1.60}

# print(dictionary_person)
# person_2 = dict(name='Carol', age=18, height=1.60)

# print(dictionary_person.keys())
# print(dictionary_person.values())
# print(dictionary_person.items())
# Iterate over a dictionary
for item in dictionary_person.items():
    # print(item)
    print(item[1])
