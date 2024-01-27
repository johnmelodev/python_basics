# Inheritance
class Camera:
    def __init__(self, brand, megapixels):
        self.brand = brand
        self.megapixels = megapixels

    def take_photo(self):
        print(f'Photo taken with the {self.brand} camera with a quality of {
              self.megapixels} megapixels')


class CellphoneCamera(Camera):
    def __init__(self, brand, megapixels, number_of_cameras):
        super().__init__(brand, megapixels)
        self.number_of_cameras = number_of_cameras

    def apply_filter(self, filter):
        print(f'Applying {filter} filter')


# Usage example
cellphone_camera = CellphoneCamera('Sony', '25MP', 4)
cellphone_camera.apply_filter('Blue')
cellphone_camera.take_photo()
