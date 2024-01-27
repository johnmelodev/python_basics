class Person:
    def introduce(self, name, age=None, profession=None):
        if age and profession != None:
            print(f'{name}, {age}, {profession}')
        elif age != None:
            print(f'{name}, {age}')
        elif profession != None:
            print(f'{name}, {profession}')
        else:
            print(name)


# Usage example
person = Person()
person.introduce('Amanda')
person.introduce('Amanda', 18)
person.introduce('Amanda', 18, "Programmer")
