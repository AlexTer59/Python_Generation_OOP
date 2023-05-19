class Numbers:
    def __init__(self):
        self.list = []

    def add_number(self, number):
        self.list.append(number)

    def get_even(self):
        return list(filter(lambda num: num % 2 == 0, self.list))

    def get_odd(self):
        return list(filter(lambda num: num % 2 != 0, self.list))

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())