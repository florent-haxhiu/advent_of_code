def read_file(file_name: str) -> list:
    with open(file_name, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def convert_list_into_readable_format(curr_list: list):
    new_list = ''.join(curr_list).split(' ')
    new_list = [num for num in new_list if num]
    return set([int(num) for num in new_list])


def find_total_points(file_name: str) -> int:
    file_data: list = read_file(file_name)
    total = 0

    for line in file_data:
        all_numbers = ''.join(line).split(':')
        numbers = ''.join(all_numbers[1]).split('|')
        winning_numbers: set = convert_list_into_readable_format(numbers[1])
        guessed_numbers: set = convert_list_into_readable_format(numbers[0])

        len_of_guessed = len(guessed_numbers)
        len_of_winning = len(winning_numbers)

        diff = guessed_numbers.difference(winning_numbers)
        print(diff)
        temp_num = 1

        diff_between_sets = len_of_guessed - len(diff)
        if diff_between_sets == 0:
            continue

        for i in range(1, diff_between_sets):
            temp_num *= 2

        print(temp_num)

        total += temp_num

    return total

print(find_total_points('part_one.txt'))

