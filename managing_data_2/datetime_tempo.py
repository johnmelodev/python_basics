# define when the program will run date and time
from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# create a datetime

app_launch = datetime(2021, 5, 28)
print(app_launch)

# I want to receive the launch date of my application
launch_date = datetime.strptime(
    input('when should we launch the application?'), '%d/%m/%Y')
print(type(launch_date))

# if you want to know how long until the launch
# until the launch
current_date = datetime.now()
deadline = launch_date - current_date
print(deadline.days/7)
