from time import time

def solve(input):
    with open(input) as file:
        input = file.read().split()
        r0 = len(input)
        c0 = len(input[0])
        grid = {}
        for r, line in enumerate(input):
            for c, val in enumerate(line):
                grid[(r, c)] = val
    dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    max_ = 4
    total = 0
    for loc, val in grid.items():
        if val != '@':
            continue
        count_ = 0
        for dir in dirs:
            r, c = tuple(sum(x) for x in zip(loc, dir))
            if r < 0 or r >= r0 or c < 0 or c >= c0:
                continue
            if grid[(r, c)] == '@':
                count_ += 1
        if count_ < max_:
            total += 1
    return total
if __name__ == '__main__':
    input = 'day_4/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 1351
    print('runtime =', round(time() - t0, 3), 's') # 0.823 s