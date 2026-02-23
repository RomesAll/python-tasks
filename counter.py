

class Counter:
    def __init__(self):
        self.counter = 0
    def increase(self, amount=1):
        self.counter += amount
    def decrease(self, amount=1):
        self.counter -= amount
    def getValue(self):
        return self.counter