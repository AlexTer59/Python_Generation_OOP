class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, horizontal_end, vertical_end):
        return True if abs(self.horizontal_dict[horizontal_end] - self.horizontal_dict[self.horizontal]) == 2 and abs(
            vertical_end - self.vertical) == 1 or abs(
            self.horizontal_dict[horizontal_end] - self.horizontal_dict[self.horizontal]) == 1 and abs(
            vertical_end - self.vertical) == 2 else False

    def move_to(self, horizontal, vertical):
        if knight.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        vertical = 8 - self.vertical
        board = [['.' for _ in range(8)] for _ in range(8)]
        board[vertical][self.horizontal_dict[self.horizontal]] = 'N'
        for i in range(-2, 3):
            if i == 0:
                continue
            if 0 <= self.horizontal_dict[self.horizontal] + i <= 7 and 0 <= vertical + (3 - abs(i)) <= 7:
                board[vertical + (3 - abs(i))][self.horizontal_dict[self.horizontal] + i] = '*'
            if 0 <= self.horizontal_dict[self.horizontal] + i <= 7 and 0 <= vertical - (3 - abs(i)) <= 7:
                board[vertical - (3 - abs(i))][self.horizontal_dict[self.horizontal] + i] = '*'

        for i in range(8):
            print(*board[i], sep='')

knight = Knight('a', 1, 'white')

knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()
