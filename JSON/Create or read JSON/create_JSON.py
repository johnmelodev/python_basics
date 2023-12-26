# It's better to create a Json file externally in the same folder and import it. This helps to organize and format it in an individual file.
# like the example below
import json

computer_json = """{
    "brand": "Dell",
    "price": 15000
}"""
# how to read a JSON string
data = json.loads(computer_json)
print(data["price"])
# save JSON string to JSON File

with open('computer.json', 'w', encoding='utf-8') as json_file:
    json.dump(computer_json, json_file)

# To read a JSON file in python

with open('computer.json', encoding='utf-8') as json_file:
    computer_json_string = json.load(json_file)
# Converting the JSON string back to a dictionary
    computer_json_dictionary = json.loads(computer_json_string)

# Printing the dictionary
    print(computer_json_dictionary["brand"])
