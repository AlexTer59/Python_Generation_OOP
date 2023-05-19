class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) == 0 or not new_name.isalpha():
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if type(new_age) != int or 110 < new_age or new_age < 0:
            raise ValueError('Некорректный возраст')
        self._age = new_age

user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
