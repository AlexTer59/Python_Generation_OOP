class Wordplay:
    def __init__(self, words=[]):
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        return [i for i in self.words if set(i).issubset(args)]

    def avoid(self, *args):
        return [i for i in self.words if set(i).isdisjoint(args)]


words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)