# decorators
from datetime import datetime


def my_decorator(function):
    def wrapper():
        print('Before')
        function()
        print('After')
    return wrapper


@my_decorator
def congratulate():
    print('Congratulations!!!!!')

# or
# result = my_decorator(congratulate)
# congratulate()

# example:


def monitor_time(function):
    def monitor():
        print(datetime.now())
        function()
        print(datetime.now())
    return monitor


@monitor_time
def download_songs():
    print('Downloading songs')


download_songs()
