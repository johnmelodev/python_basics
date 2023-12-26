import json
# EXAMPLE 1
with open('/Users/joaomelo/Programming/python_basics/JSON/read Jason files/example1.json', encoding='utf-8') as json_file:
    data = json.load(json_file)  # convert a JSON file to a string
    print(data['name'])
# or

# import json

# with open('example1.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)

# If you want to search for a specific element of the JSON file. go to the terminal and search data["name"]
# search by index

# EXAMPLE 2

with open('/Users/joaomelo/Programming/python_basics/JSON/read Jason files/example2.json', encoding='utf-8') as json_file:
    data = json.load(json_file)  # convert a JSON file to a string
    print(data["permissions"][1])

# EXAMPLE 3

with open('/Users/joaomelo/Programming/python_basics/JSON/read Jason files/example3.json', encoding='utf-8') as json_file:
    data = json.load(json_file)  # convert a JSON file to a string
    print(data["users"][0]["phone"])
# If you want to know if, for example, Douglas is Admin
    print(data["users"][1]["admin"])

# EXAMPLE 4

with open('/Users/joaomelo/Programming/python_basics/JSON/read Jason files/example4.json', encoding='utf-8') as json_file:
    data = json.load(json_file)  # convert a JSON file to a string
    print(data["users"][1]["plan"]["price"])

# EXAMPLE 5

with open('/Users/joaomelo/Programming/python_basics/JSON/read Jason files/example5.json', encoding='utf-8') as json_file:
    data = json.load(json_file)  # convert a JSON file to a string
    # as it is a direct list without a name we start directly without the users
    print(data[0]["admin"])
