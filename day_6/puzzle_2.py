from time import time
import copy

def solve(input):
    with open(input) as file:
        input = [list(x) for x in file.read().split('\n')]
    rows, cols, idxs = len(input), len(input[0]), []
    for c in range(cols):
        column = [input[r][c] for r in range(rows)]
        if all(char == ' ' for char in column):
            idxs.append(c)
    
    clean_input = []
    for r in input:
        copy_idxs = [-1] + copy.deepcopy(idxs) + [len(r)]
        clean_input.append([r[copy_idxs[i] + 1:copy_idxs[i+1]] for i in range(len(copy_idxs)-1)])
    for c in clean_input[-1]:
        c[:] = c[0] * len(c)
        
    rows, cols, total = len(clean_input), len(clean_input[0]), 0
    for c in range(cols):
        cephalopod_nums  = [clean_input[r][c] for r in range(rows - 1)]
        op = clean_input[rows - 1][c][0]
        human_nums = [''.join(chars) for chars in zip(*cephalopod_nums)]
        equation = ''.join([num.replace(' ', '') + op for num in human_nums])
        total += eval(equation[:-1])
    return total

if __name__ == '__main__':
    input = 'day_6/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 8907730960817
    print('runtime =', round(time() - t0, 3), 's') # 0.055 s