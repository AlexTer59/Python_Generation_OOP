class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n

    def get_result(self):
        if self.right > self.left:
            return 'Правая чаша тяжелее'
        if self.right < self.left:
            return 'Левая чаша тяжелее'
        return 'Весы в равновесии'


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

