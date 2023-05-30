import os

import hangman


def test_random_word_no_scpl():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.random_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_random_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.random_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_maskword_single_letter():
    secret_word = "elephant"
    guesses = ["e"]
    ret =hangman.maskword(secret_word, guesses)
    assert ret == "e-e-----"