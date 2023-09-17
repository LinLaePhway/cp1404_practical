import random

from cars import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
