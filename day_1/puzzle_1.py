from time import time

def solve(input):
    with open(input) as file:
        dirs = [(y[0], int(y[1:])) for y in [x.strip() for x in file.readlines()]]
    start = 50
    max = 100
    count = 0
    for dir, num in dirs:
        if dir == 'L':
            start = (start - num) % max
        else:
            start = (start + num) % max
        if start == 0:
            count += 1
    return count

if __name__ == '__main__':
    input = 'day_1/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 1141
    print('runtime =', time() - t0, 's') # 0.00395965576171875 s