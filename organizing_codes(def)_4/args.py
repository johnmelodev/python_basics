def add(*values, b):
    print(values)
    for value in values:
        b += value
    print(b)


add(10, 20, 5, b=5)
# *args
