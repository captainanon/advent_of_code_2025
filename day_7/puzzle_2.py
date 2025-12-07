from time import perf_counter
from functools import cache

@cache
def search(r, c):
    global input
    rows, cols, curr, timelines = len(input) - 1, len(input[0]), input[r][c], 0
    if r == rows:
        return 1
    elif curr == '^':
            if c - 1 >= 0:
                timelines += search(r + 1, c - 1)
            if c + 1 < cols:
                timelines += search(r + 1, c + 1)
    else:
        timelines += search(r + 1, c)
    return timelines

def get_input(input):
    with open(input) as file:
        input = file.read().split('\n')
    return input

if __name__ == '__main__':
    start_time = perf_counter()
    input = get_input('day_7/input.txt', )
    start = input[0].index('S')
    answer = search(0, start)
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 62943905501815
    print('runtime =', runtime, 's') # 0.008 s