from abc import ABC, abstractmethod


class Monitor(ABC):
    @abstractmethod
    def increase_brightness(self, value):
        pass

    @abstractmethod
    def decrease_brightness(self, value):
        pass


class FullHDMonitor(Monitor):
    def increase_brightness(self, value):
        print(f'Increasing brightness by {value} points')

    def decrease_brightness(self, value):
        print(f'Decreasing brightness by {value} points')


# example
monitor = FullHDMonitor()
monitor.increase_brightness(5)
monitor.decrease_brightness(5)
