import random

guesses = 0
correct = 1
wrong= 2


def random_word(wordfile="/usr/share/dict/words"):
    words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >= 5:
                words.append(i)
    return random.choice(words)


def maskword(secret_word, guesses):
    op = []
    for i in secret_word:
        if i in guesses:
            op.append(i)
        else:
            op.append("-")
    return "".join(op)


def update_status(secret_word, guesses, turns_remaining):
    masked_word = maskword(secret_word, guesses)
    guessed_letters = " ".join(guesses)
    return f"""Secret word:{masked_word}
Guesses : {guessed_letters}
Remaining turns : {turns_remaining}"""


def check(secret_word, guesses, turns_remaining, new_guess):
    if new_guess in guesses:
        return guesses, turns_remaining
    else:
        guesses.append(new_guess)
        if new_guess in secret_word:
            return correct, turns_remaining
        else:
            return wrong, turns_remaining - 1


def game_over(secret_word, guesses, turns_remaining):
    if turns_remaining == 0:
        return True, f"You lost! The word was {secret_word}"
    masked = maskword(secret_word, guesses)
    if "-" in masked:
        return False, None
    else:
        return True, f"You guessed it! The word was {secret_word}"


def main():
    secret_word = random_word()
    
    guesses = []
    turns_remaining = 8
    while True:
        print(update_status(secret_word, guesses, turns_remaining))
        guess = input("Enter a letter ")

        status, turns_remaining = check(secret_word, guesses, turns_remaining, guess)
        if status == guesses:
            print("You already guessed that")

        finished, message = game_over(secret_word, guesses, turns_remaining)
        if message:
            print(message)
        if finished:
            break


if __name__ == "__main__":
    main()
