class Todo:
    def __init__(self, things=[]):
        self.things = things

    def add(self, todo, priority):
        tuple_todo = (todo, priority)
        self.things.append(tuple_todo)

    def get_by_priority(self, priority):
        return [i[0] for i in self.things if i[1] == priority]

    def get_low_priority(self):
        return [i[0] for i in self.things if i[1] == min(map(lambda x: x[1], self.things))]

    def get_high_priority(self):
        return [i[0] for i in self.things if i[1] == max(map(lambda x: x[1], self.things))]

todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())