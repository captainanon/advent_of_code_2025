from time import perf_counter
from math import prod

def solve(input):
    with open(input) as file:
        preprocessing = file.read().split('\n\n')
        presents = {int(k): v.count('#') for line in preprocessing[:-1] for k, v in [line.split(':\n')]}
        areas = [(prod(map(int, k.split('x'))), tuple(map(int, v.split(' ')))) for line in preprocessing[-1].split('\n') for k, v in [line.split(': ')]]
   
    count, unknown, max_area = 0, 0, 9
    for area_of_tree, vals in areas:
        area_of_presents = sum([val * presents[idx] for idx, val in enumerate(vals)])
        area_of_presents_max = sum(vals) * max_area
        if area_of_presents > area_of_tree:
            pass
        elif area_of_presents_max <= area_of_tree:
            count += 1
        else:
            unknown += 1
        
    return count if unknown == 0 else 'unknown'

if __name__ == '__main__':
    start_time = perf_counter()
    answer = solve('day_12/input.txt')
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 591
    print('runtime =', runtime, 's') # 0.003 s