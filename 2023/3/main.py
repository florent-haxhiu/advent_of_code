import math


def read_file(file_name):
    with open(file_name, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


file_data = read_file('part_two.txt')


def neighbors(x, y):
    for i in [-1, 0, 1]:
        a = x + i
        if a < 0 or a >= len(file_data):
            continue
        for j in [-1, 0, 1]:
            b = y + j
            if b < 0 or b >= len(file_data[a]):
                continue
            if i == 0 and j == 0:
                continue
            yield file_data[a][b], a, b


def find_star(stars, i, j):
    for n, i2, j2 in neighbors(i, j):
        if n == '*':
            stars.add((i2, j2))
    return stars


num = False

stars = set()
acc = []
den = []
result = {}

current = 0
for i, l in enumerate(file_data):
    for j, c in enumerate(l):
        if num:
            if c.isnumeric():
                current = current * 10 + int(c)
                stars = find_star(stars, i, j)
            else:
                for x, y in stars:
                    if x not in result:
                        result[x] = {}
                    if y not in result[x]:
                        result[x][y] = []
                    result[x][y].append(current)
                num = False
                stars = set()
        else:
            if c.isnumeric():
                num = True
                current = int(c)
                stars = find_star(stars, i, j)
final_result = 0
for i in result:
    for j in result[i]:
        v = result[i][j]
        size = len(v)
        if size == 2:
            final_result = final_result + math.prod(v)
print(final_result)
