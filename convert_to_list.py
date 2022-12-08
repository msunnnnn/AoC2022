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

