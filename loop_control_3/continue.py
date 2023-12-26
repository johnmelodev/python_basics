for number in range(100):
    if number % 2 == 0:
        print(number)
    else:
        continue
# break to interrupt the iteration
for number in range(100):
    if number % 2 == 0:
        print(number)
    else:
        break

fruits = ['Apple', 'Mango', 'Orange', 'Strawberry']
for fruit in fruits:
    if fruit == 'Mango':
        continue
    print(f'{fruit} added to diet')


fruits = ['Apple', 'Mango', 'Orange', 'Strawberry']
for fruit in fruits:
    if fruit == 'Orange':
        break
    print(f'{fruit} added to diet')


styles = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for style in styles:
    if style == 'Rap':
        continue
    print(style)

styles = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for style in styles:
    if style == 'Rock':
        break
    print(style)
