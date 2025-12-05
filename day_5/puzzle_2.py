from time import time
import copy

def solve(input):
    with open(input) as file:
        input = file.read().split('\n\n')
        ranges = [x.split('-') for x in input[0].split('\n')]
        go = 1
        while go:
            updated_ranges = copy.deepcopy(ranges)
            go = 0
            for i in range(len(ranges)):
                for j in range(i + 1, len(ranges)):
                    s0 = int(ranges[i][0])
                    e0 = int(ranges[i][1])
                    s1 = int(ranges[j][0])
                    e1 = int(ranges[j][1])
                    if s0 <= s1 and e0 >= e1: # second range is subset of first range
                        updated_ranges.pop(j)
                        go = 1
                        break
                    elif s0 >= s1 and e0 <= e1: # first range is subset of second range
                        updated_ranges.pop(i)
                        go = 1
                        break
                    elif s0 >= s1 and s0 <= e1 and e0 >= e1: # overlap - use start of second range, end of first range
                        updated_ranges[i][0] = updated_ranges[j][0]
                        updated_ranges.pop(j)
                        go = 1
                        break
                    elif s0 <= s1 and e0 >= s1 and e0 <= e1: # overlap- use start of first range, end of second range
                        updated_ranges[i][1] = updated_ranges[j][1]
                        updated_ranges.pop(j)
                        go = 1
                        break
                if go:
                    break
            ranges = copy.deepcopy(updated_ranges)
        total = 0
        for range_ in ranges:
            total += int(range_[1]) - int(range_[0]) + 1
    return total

if __name__ == '__main__':
    input = 'day_5/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 353507173555373
    print('runtime =', round(time() - t0, 3), 's') # 0.254 s