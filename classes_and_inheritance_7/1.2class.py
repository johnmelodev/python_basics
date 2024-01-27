# Class
class Computer:
    def __init__(self, brand, ram_memory, video_card):
        self.brand = brand
        self.ram_memory = ram_memory
        self.video_card = video_card


# Usage examples
computer1 = Computer('Asus', '8GB', 'Nvidia')
print(computer1.brand)
print(computer1.ram_memory)
print(computer1.video_card)

computer2 = Computer('Dell', '4GB', 'ATI')
print(computer2.brand)
print(computer2.ram_memory)
print(computer2.video_card)
