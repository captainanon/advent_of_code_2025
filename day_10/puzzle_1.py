from time import perf_counter
from collections import Counter
from itertools import combinations_with_replacement

def solve(input):
    with open(input) as file:
        lines = [x.split(' ')for x in file.read().split('\n')]
    
    results = []
    for line in lines:
        lights = [1 if x == '#' else 0 for x in list(line[0][1:-1])]
        buttons_temp = [x[1:-1] for x in line[1:-1]]
        buttons = [tuple(map(int, x.split(','))) for x in buttons_temp]
        i = 1
        while True:
            combos = list(combinations_with_replacement(buttons, i))
            for outer in combos:
                nums = [num for inner in outer for num in inner]
                counted = dict(Counter(nums))
                result = []
                for idx in range(len(lights)):
                    if idx not in counted:
                        result.append(0)
                    else:
                        result.append(0 if counted[idx] % 2 == 0 else 1)
                if result == lights:
                    results.append(i)
                    break
            else:
                i += 1
                continue
            break
    
    return sum(results)

if __name__ == '__main__':
    start_time = perf_counter()
    answer = solve('day_10/input.txt')
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 558
    print('runtime =', runtime, 's') # 1.39 s