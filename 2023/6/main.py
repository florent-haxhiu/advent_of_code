file = open('input.txt', 'r').readlines()

time = int(file[0].split(':')[1].replace(' ', ''))
distance = int(file[1].split(':')[1].replace(' ', ''))

total = 1

win = 0

for x in range(0, time):
    distance_travelled = (time - x) * x
    if distance_travelled > distance:
        win += 1

total *= win

print(total)
