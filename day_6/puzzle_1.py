from time import time
from collections import defaultdict

def solve(input):
    with open(input) as file:
        input = [x.split() for x in file.read().split('\n')]
        rows = len(input)
        cols = len(input[0])
        equations = defaultdict(str)
        for r in range(rows - 1):
            for c in range(cols):
                num = input[r][c]
                op = input[rows - 1][c]
                equations[c] += num + op
    return sum([eval(x[:-1]) for x in equations.values()])

if __name__ == '__main__':
    input = 'day_6/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 4805473544166
    print('runtime =', round(time() - t0, 3), 's') # 0.011 s