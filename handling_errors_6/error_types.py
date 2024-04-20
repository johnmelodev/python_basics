# internet = None
# try:
#     print('Making connection with ' + internet)
# except TypeError as error:
#     print('There is no internet connection')
# finally:
#     print('Undoing the purchase!')

try:
    value = int(input('Enter a value: '))
    print(value / 0)
except ZeroDivisionError as error:
    print('It is not possible to divide by zero!')
except ValueError as error:
    print('Please enter only numbers')
finally:
    print('The operation was canceled!')
