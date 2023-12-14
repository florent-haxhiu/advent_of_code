from typing import List

file = open('./part_one.txt').read().strip().split("\n\n")
print(file)

seeds = [int(x) for x in file[0].replace('seeds: ', '').split(' ')]

maps = [
    [[int(y) for y in x.split(' ')] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
]


def x_to_y(step: int, m: List[List[int]]) -> int:
    for destination_range_start, source_range_start, range_start in m:
        if source_range_start <= step < source_range_start + range_start:
            step = destination_range_start + (step - source_range_start)
            break
    return step


smallest_location = float('inf')

for seed in seeds:
    for m in maps:
        seed = x_to_y(seed, m)
    smallest_location = min(smallest_location, seed)

print(smallest_location)
