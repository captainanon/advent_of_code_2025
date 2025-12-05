from time import time

def solve(input):
    with open(input) as file:
        input = file.read().split('\n\n')
        ranges = [x.split('-') for x in input[0].split('\n')]
        ingredient_ids = input[1].split()
        total = 0
        for ingredient_id in ingredient_ids:
            for range_ in ranges:
                if eval(range_[0] + ' <= ' + ingredient_id + ' <= ' + range_[1]):
                    total += 1
                    break
    return total

if __name__ == '__main__':
    input = 'day_5/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 623
    print('runtime =', round(time() - t0, 3), 's') # 1.225 s