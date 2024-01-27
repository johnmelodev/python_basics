# Common methods
# Class Methods
# Static Methods

# Common methods
class Computer:
    operating_system = 'Windows 10'

    def __init__(self, brand, ram_memory, video_card):
        self.brand = brand
        self.ram_memory = ram_memory
        self.video_card = video_card

    def display_computer_data(self):
        print(self.brand, self.ram_memory,
              self.video_card, self.operating_system)


# Class Methods

class Computer:
    operating_system = 'Windows 10'

    def __init__(self, brand, ram_memory, video_card):
        self.brand = brand
        self.ram_memory = ram_memory
        self.video_card = video_card

    def display_computer_data(self):
        print(self.brand, self.ram_memory,
              self.video_card, self.operating_system)

    @classmethod
    def office_computer(cls, ram_memory):
        return cls('Dell', ram_memory, 'Low Cost Video Card')

    @classmethod
    def heavy_configuration_computer(cls, ram_memory):
        return cls('Dell', ram_memory, 'High Level Video Card')


# Configuration for office client
computer1 = Computer.office_computer('8GB')
computer1.display_computer_data()
print('#########')

# Configuration for heavy client (games, videos, 3D)
computer2 = Computer.heavy_configuration_computer('16GB')
computer2.display_computer_data()


# Static Methods

class Computer:
    operating_system = 'Windows 10'

    def __init__(self, brand, ram_memory, video_card):
        self.brand = brand
        self.ram_memory = ram_memory
        self.video_card = video_card

    def display_computer_data(self):
        print(self.brand, self.ram_memory,
              self.video_card, self.operating_system)

    @classmethod
    def office_computer(cls, ram_memory):
        return cls('Dell', ram_memory, 'Low Cost Video Card')

    @classmethod
    def heavy_configuration_computer(cls, ram_memory):
        return cls('Dell', ram_memory, 'High Level Video Card')

    @staticmethod
    def runs_heavy_programs(ram_memory):
        if ram_memory >= 8:
            return True
        else:
            return False


print(Computer.runs_heavy_programs(10))
