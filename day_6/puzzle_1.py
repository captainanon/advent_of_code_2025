from time import time

def solve(input):
    with open(input) as file:
        input = [x.split() for x in file.read().split('\n')]
    rows, cols = len(input), len(input[0])
    total = 0
    for c in range(cols):
        equation = ''.join([input[r][c] + input[rows - 1][c] for r in range(rows - 1)])
        total += eval(equation[:-1])
    return total

if __name__ == '__main__':
    input = 'day_6/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 4805473544166
    print('runtime =', round(time() - t0, 3), 's') # 0.011 s