class Computer:
    operating_system = 'Windows 10'

    def __init__(self, brand, ram_memory, video_card):
        self.brand = brand
        self.ram_memory = ram_memory
        self.video_card = video_card

    def turn_on(self):
        print('Turning on the computer')


# Assigning values to the class variable 'operating_system'
Computer.operating_system = 'Windows'

computer = Computer('Dell', '8GB', 'NVIDIA')
computer.brand = 'ASUS'
print(computer.brand)
print(computer.operating_system)

# Assigning a new value to the class variable 'operating_system'
Computer.operating_system = 'Mac'
computer2 = Computer('Asus', '2GB', 'ATI')
print(computer2.operating_system)
