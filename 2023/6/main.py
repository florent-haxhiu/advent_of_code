import re

file = open('input.txt', 'r').readlines()

times = re.findall(r'\d+', file[0])
distances = re.findall(r'\d+', file[1])

total = 1

for time, distance in zip(times, distances):

    win = 0

    for x in range(0, int(time)):
        distance_travelled = (int(time) - x) * x
        if distance_travelled > int(distance):
            win += 1

    total *= win

print(total)
