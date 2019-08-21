from random import randint
from string import ascii_letters

def get_word(length=1):
    return ''.join(
        ascii_letters[randint(0, len(ascii_letters) - 1)]
        for x in range(length)
    )


with open("heavy.txt") as f:
    # for _ in range(100000):
    #     f.write(' '.join(get_word(30) for _ in range(7)) + "\n")
    # print(next(f))
    # print(next(f))
    next(f); next(f)
    content = f.readlines()
    print(len(content), type(content))
