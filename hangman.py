import random

ALREADY_GUESSED = 0
CORRECT = 1
WRONG = 2

def random_word(wordfile="/usr/share/dict/words"):
    words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >=5:
                words.append(i)
    return random.choice(words)