def read_file(file_name: str):
    with open(file_name, 'r') as f:
        file_data = [line.strip() for line in f.readlines()]
    return file_data

file_data = read_file('part_one.txt')
nums_in_word = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_calibration(file_data: list):
    total = 0
    for data in file_data:
        nums = [char for char in data if char.isnumeric()]
        if len(nums) == 1:
            total += int(str(nums[0]) + str(nums[0]))
        else:
            total += int(str(nums[0]) + str(nums[-1]))
    return total

print(find_calibration(file_data))
