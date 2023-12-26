for number in range(5):
    print('loading', number)

for number in range(18, 111):
    print('we are at', number)

# if you want it to skip by 2 for example

for number in range(1, 20, 2):
    print('loading', number)

# print several at once
names = ['jeff', 'carl', 'jean', 'luke']
for name in names:
    print(name)

countries = ['brazil', 'india', 'united states']
seasons_of_the_year = ['spring', 'summer', 'autumn', 'winter']
for country in countries:
    for season in seasons_of_the_year:
        print(f'{country} {season}')


cellphones = ['Asus', 'Samsung', 'Sony', 'Iphone']
versions = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']
for cellphone in cellphones:
    for version in versions:
        print(f'{cellphone} {version}')
