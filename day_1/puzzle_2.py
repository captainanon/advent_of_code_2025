from time import time

def solve(input):
    with open(input) as file:
        dirs = [(y[0], int(y[1:])) for y in [x.strip() for x in file.readlines()]]
    start = 50
    max = 100
    count = 0
    for dir, num in dirs:
        if dir == 'L':
            past_zero = ((-start % max) + num) // max
            start = (start - num) % max
        else:
            past_zero = (start + num) // max 
            start = (start + num) % max
        count += past_zero
    return count

if __name__ == '__main__':
    input = 'day_1/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 6634
    print('runtime =', time() - t0, 's') # 0.004994869232177734 s