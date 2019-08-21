from random import randint
from string import ascii_letters
WORD_LENGTH = 30
WORDS_PER_LINE = 10
LINES_COUNT = 300000

def get_word(length=1):
    return ''.join(
        ascii_letters[randint(0, len(ascii_letters) - 1)]
        for x in range(length)
    )


with open("heavy.txt", "a+") as f:
    for _ in range(LINES_COUNT):
        f.write(' '.join(get_word(WORD_LENGTH) for _ in range(WORDS_PER_LINE)) + "\n")
