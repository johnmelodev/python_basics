import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Enter your email: ')
    password = int(input('Enter your bank password: '))
    if password == 1234:
        logging.info(f'{email} entered their bank account')
except ValueError as error:
    print('Please enter only numbers')
    logging.warning(error)
