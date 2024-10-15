import random

class GenerateNumber():
    def __init__(self):
        pass
    # this function will give us back a number between 1 to 100
    def generate_random_number(self, start, end):
        number = random.randint(start,end)
        return number
