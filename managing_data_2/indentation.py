import time


def ThinkFor10Seconds():
    print('thinking')
    time.sleep(10)
    print('Remembered!')


if 10 > 5:
    print('10 is greater than 5')


class Welcome():
    def __init__(self):
        print('Welcome')


hi = Welcome()
