from time import time

def solve(input):
    with open(input) as file:
        num_batts = 2
        total = 0
        for line in file.read().split():
            bank = list(map(int, list(line)))
            batts = [] 
            end_idx = -(num_batts - 1)
            for i in range(0, num_batts):
                if end_idx == 0:
                    maximum = max(bank)
                else:
                    maximum = max(bank[:end_idx])
                batts.append(maximum)
                idx = bank.index(maximum)
                bank = bank[idx + 1:]
                end_idx += 1
            jolts = ''.join(list(map(str, batts)))
            total += int(jolts)
    return total
if __name__ == '__main__':
    input = 'day_3/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 17100
    print('runtime =', time() - t0, 's') # 0.0029802322387695312 s