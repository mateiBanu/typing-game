import random

class WordSet:

    def __init__(self, file_path: str):
        self._word_set = []

        file = open(file_path, "r")
        for line in file:
            self._word_set.append(line[:-1])
    
    def get(self):
        return random.choice(self._word_set)

