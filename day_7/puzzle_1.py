from time import perf_counter
from functools import cache

@cache
def search(r, c):
    global input, splitter
    rows, cols, curr = len(input) - 1, len(input[0]), input[r][c]
    if r == rows:
        return
    if curr == '^':
        splitter.add((r, c))
        if c - 1 >= 0:
            search(r + 1, c - 1)
        if c + 1 < cols:
            search(r + 1, c + 1)
    else:
        search(r + 1, c)
    return

def get_input(input):
    with open(input) as file:
        input = file.read().split('\n')
    return input

if __name__ == '__main__':
    start_time = perf_counter()
    input = get_input('day_7/input.txt')
    start = input[0].index('S')
    splitter = set()
    search(0, start)
    answer = len(splitter)
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 1667
    print('runtime =', runtime, 's') # 0.008 s