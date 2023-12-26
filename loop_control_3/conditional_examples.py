# conditional examples

work_finished = False
if work_finished == True:
    print("Let's go out")

# else = otherwise
else:
    print("I can't go out now")

number_delays = 2

if number_delays >= 3:
    print('Go to the office')
elif number_delays == 2:
    print('This is your second delay')
elif number_delays == 1:
    print('This is your first delay')
else:
    print('You can enter')


speed = 100
if speed <= 50:
    print('You were not fined')
elif speed >= 51 and speed <= 60:
    print('You got a 2-point fine')
elif speed >= 61 and speed <= 75:
    print('You got a 3-point fine')
else:
    print('You got a 7-point fine')

# Or do something that looks like this called "chaining"

speed = 55
if speed <= 50:
    print('You were not fined')
elif 51 <= speed <= 60:
    print('You got a 2-point fine')

hair_length = 26
if hair_length <= 20:
    print('Pay $50.00')
elif hair_length >= 21 and hair_length <= 30:
    print('Pay $70.00')
elif hair_length >= 31 and hair_length <= 50:
    print('Pay $100.00')
else:
    print('Please consult at the reception')


# chaining
hair_length = 54
if hair_length <= 20:
    print('Price of $50.00')
elif 21 <= hair_length <= 30:
    print('Price of $70.00')
elif 31 <= hair_length <= 50:
    print('Price of $100.00')
else:
    print('please consult at the reception')
