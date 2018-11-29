
def my_enumerate(iterable, start=0):
    result = []
    for element in iterable:
        result.append((start, element))
        start += 1
    return result

if __name__ == '__main__':
    en = my_enumerate(['one', 'two', 'three', 'four'])
    for pos in en:
        print(pos[0], pos[1])
