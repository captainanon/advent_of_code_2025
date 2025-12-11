from time import perf_counter
from functools import cache

def get_graph(input):
    with open(input) as file:
        lines = file.read().split('\n')
        partially_processed_lines = [line.split(': ') for line in lines]
        graph = {k: v.split(' ') for k, v in partially_processed_lines}
    
    return graph

@cache 
def solve(curr_node):
    if curr_node == 'out':
        return 1
    
    if curr_node not in graph:
        return 0

    total = 0
    for neighbor in graph[curr_node]:
        total += solve(neighbor)
        
    return total

if __name__ == '__main__':
    start_time = perf_counter()
    graph = get_graph('day_11/input.txt')
    start_node = 'you'
    answer = solve(start_node)
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 749
    print('runtime =', runtime, 's') # 0.001 s