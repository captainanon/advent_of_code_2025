from time import perf_counter
from functools import cache

def get_graph(input):
    with open(input) as file:
        lines = file.read().split('\n')
        partially_processed_lines = [line.split(': ') for line in lines]
        graph = {k: v.split(' ') for k, v in partially_processed_lines}
    
    return graph

@cache 
def solve(curr_node, curr_devices):
    if curr_node == 'out':
        return 1 if sum(curr_devices) == 2 else 0
    
    if curr_node not in graph:
        return 0

    total = 0
    for neighbor in graph[curr_node]:
        new_devices = (1, curr_devices[1]) if neighbor == 'dac' else (curr_devices[0], 1) if neighbor == 'fft' else curr_devices
        total += solve(neighbor, new_devices)
        
    return total

if __name__ == '__main__':
    start_time = perf_counter()
    graph = get_graph('day_11/input.txt')
    start_node = 'svr'
    start_devices = (0, 0)
    answer = solve(start_node, start_devices)
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 420257875695750
    print('runtime =', runtime, 's') # 0.003 s