# Magic Methods (dunder methods (double underscore))
class Person:
    def __init__(self):
        self.name = 'I am a person'
        self.skills = ['Skill 1', 'Skill 2', 'Skill 3']

    # Representation for programmers (called with repr(person) method)
    def __repr__(self):
        return 'Person class with properties name and skills'

    # What should return the quantity, the class (called with len(person) method)
    def __len__(self):
        # len(person)
        return len(self.skills)

    def __str__(self):
        return f'{self.name} with the skills {self.skills}'


# Usage example
person = Person()
print(person.name)
print(repr(person))
print(len(person))
print(person)
print(dir(person))
