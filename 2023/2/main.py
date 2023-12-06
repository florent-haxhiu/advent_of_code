MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_file(file_name: str):
    with open(file_name, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data

file_data = read_file('part_one.txt')

def find_sum_of_game_ids(data: list):
    game_ids = []
    for line in data:
        joined_lines = "".join(line.split(':', maxsplit=1)[1]).strip()
        split_lines = joined_lines.split(' ')
        game_id = line.split(':')[0].split(' ', maxsplit=1)[-1]

        is_valid = True
        for i in range(len(split_lines)-1):
            if split_lines[i].isdigit() and split_lines[i+1].startswith('blue'):
                if int(split_lines[i]) > MAX_BLUE:
                    is_valid = False
                    break
            elif split_lines[i].isdigit() and split_lines[i+1].startswith('green'):
                if int(split_lines[i]) > MAX_GREEN:
                    is_valid = False
                    break
            elif split_lines[i].isdigit() and split_lines[i + 1].startswith('red'):
                if int(split_lines[i]) > MAX_RED:
                    is_valid = False
                    break
            print(split_lines[i])
        if is_valid:
            game_ids.append(int(game_id))
    return sum(game_ids)

def find_the_min_number_of_cubes_per_color(data: list):
    total = 0
    for line in data:
        split_lines = "".join(line.split(':', maxsplit=1)[1]).strip().split(' ')

        min_green = find_first_color(split_lines, 'green')
        min_red = find_first_color(split_lines, 'red')
        min_blue = find_first_color(split_lines, 'blue')

        for i in range(len(split_lines)-1):
            if split_lines[i].isdigit() and split_lines[i+1].startswith('blue'):
                min_blue = max(int(split_lines[i]), min_blue)
            elif split_lines[i].isdigit() and split_lines[i+1].startswith('green'):
                min_green = max(int(split_lines[i]), min_green)
            elif split_lines[i].isdigit() and split_lines[i+1].startswith('red'):
                min_red = max(int(split_lines[i]), min_red)

        total += (min_blue * min_red * min_green)

    return total

def find_first_color(line, color):
    for i in range(len(line)-1):
        if line[i].isdigit() and line[i+1].startswith(color):
            return int(line[i])

print(find_the_min_number_of_cubes_per_color(file_data))