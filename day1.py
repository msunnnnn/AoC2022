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

"""Takes in a list of numbers
    adds elements together until current element is 0
    appends total to a new list
    sorts list from greatest to least"""

def calories_sorted(input):
    calories_list = []
    elf = 1
    calories = 0

    for i in input:
        if i == 0:
            calories_list.append(calories)
            elf += 1
            calories = 0
        else:
            calories += i

    calories_list.sort(reverse=True)
    return calories_list

def top_n(nums, n):
    total = 0
    while n != 0:
        total += nums[n-1]
        n -= 1
    return total

nums = convert_to_numbers(string_list)
sorted = calories_sorted(nums)
print(top_n(sorted, 3))



