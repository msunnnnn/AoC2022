from aocd import data

#convert to list of strings
string_list = data.splitlines()

#convert to numbers
def convert_to_numbers(nums):
    nums_list = []
    for num in nums:
        if num:
            nums_list.append(int(num))
        else:
            nums_list.append(0)
    return nums_list

def find_max_calories(input):
    dict = {}
    elf = 1
    calories = 0

    for i in input:
        if i == 0:

            dict[calories] = elf
            elf += 1
            calories = 0
        else:
            calories += i

    return max(dict.keys())

nums = convert_to_numbers(string_list)
print(find_max_calories(nums))

