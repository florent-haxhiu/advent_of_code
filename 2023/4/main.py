import re


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
        all_numbers = ''.join(line).split(':')[1]
        numbers = ''.join(all_numbers).split('|')
        winning_numbers: set = convert_list_into_readable_format(numbers[1])
        guessed_numbers: set = convert_list_into_readable_format(numbers[0])

        len_of_guessed = len(guessed_numbers)

        diff = len_of_guessed - len(guessed_numbers.difference(winning_numbers))
        temp_num = 1

        if diff == 0:
            continue

        for i in range(1, diff):
            temp_num *= 2

        print(temp_num)

        total += temp_num

    return total


def grab_card_id(card_id):
    return int(re.findall(r'\d+', card_id)[0])


def find_amount_of_scratchcards(file_name: str):
    file_data = read_file(file_name)
    amount_of_scratchcards = {}

    for line in file_data:
        card_id = grab_card_id(''.join(line).split(':')[0])
        amount_of_scratchcards[card_id] = 1

    for line in file_data:
        card_id, card_numbers = ''.join(line).split(':')
        card_id = grab_card_id(card_id)

        numbers = ''.join(card_numbers).split('|')
        guessed_numbers: set = convert_list_into_readable_format(numbers[0])
        winning_numbers: set = convert_list_into_readable_format(numbers[1])

        len_of_guessed = len(guessed_numbers)

        diff = len_of_guessed - len(guessed_numbers.difference(winning_numbers))

        for i in range(card_id + 1, card_id + diff + 1):
            if amount_of_scratchcards[card_id] != 1:
                amount_of_scratchcards[i] += amount_of_scratchcards[card_id]
            else:
                amount_of_scratchcards[i] += 1

    total = 0
    for key in amount_of_scratchcards:
        total += amount_of_scratchcards[key]

    return total


print(find_amount_of_scratchcards('part_one.txt'))
