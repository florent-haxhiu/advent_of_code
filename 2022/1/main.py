with open("actualdata", "r") as f:
    unsorted_data = f.read().splitlines()


def check_string_convert_int(data: list):
    for i in range(len(data)):
        if data[i]:
            data[i] = int(data[i])

    return data


def add_int_together():

    sorted_data = check_string_convert_int(unsorted_data)

    sum_arr = []
    set_total = 0

    for i in range(len(sorted_data)):
        if sorted_data[i]:
            set_total += sorted_data[i]
        if not sorted_data[i]:
            sum_arr.append(set_total)
            set_total = 0

    # If there still is a number in set_total, append it to the array
    sum_arr.append(set_total)

    return sum_arr


def get_the_highest_number():

    arr = add_int_together()

    biggest_number = 0

    for i in range(len(arr)):
        if biggest_number < arr[i]:
            biggest_number = arr[i]

    return biggest_number


def get_three_highest_numbers():

    arr = add_int_together()

    three_biggest_numbers = []

    arr.sort()
    arr.reverse()

    return arr[0] + arr[1] + arr[2]


print(get_three_highest_numbers())
