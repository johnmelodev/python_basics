# Class methods -> turn_on, turn_off, display_computer_data
class Computer:
    def __init__(self, brand, ram_memory, video_card):
        self.brand = brand
        self.ram_memory = ram_memory
        self.video_card = video_card

    def turn_on(self):
        print('Turning on the computer')

    def turn_off(self):
        print('Turning off')

    def display_computer_data(self):
        print(f'Computer of the brand {self.brand}, with {
              self.ram_memory} of RAM memory and that uses the video card {self.video_card}')


# Usage examples
computer1 = Computer('Asus', '32GB', 'Nvidia')
computer1.turn_on()
computer1.turn_off()
computer1.display_computer_data()

computer2 = Computer('Dell', '8GB', 'Nvidia')
computer2.turn_on()
computer2.turn_off()
computer2.display_computer_data()
