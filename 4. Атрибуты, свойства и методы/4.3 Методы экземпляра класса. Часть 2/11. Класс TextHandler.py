class TextHandler:
    def __init__(self):
        self.sentence = []

    def add_words(self, words):
        self.sentence.extend(words.split())

    def get_shortest_words(self):
        try:
            min_len = len(min(self.sentence, key=len))
            return [i for i in self.sentence if len(i) == min_len]
        except ValueError:
            return self.sentence

    def get_longest_words(self):
        try:
            max_len = len(max(self.sentence, key=len))
            return [i for i in self.sentence if len(i) == max_len]
        except:
            return self.sentence


texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
