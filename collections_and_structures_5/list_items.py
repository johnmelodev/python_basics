values = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10]
years = [2020, 2030, 2040, 2050]
# add to the end of the list
values.append(21)
print(values)
# Join lists
values.extend(years)
print(values)
# add list
new_list = values + years
print(new_list)
# to insert a new element in a list
print(years[1])
years.insert(2, 2031)
print(years)
# extract based on index
year_2020 = years.pop(0)
print(year_2020)

# Remove the item from the list
years.remove(2050)
print(years)
