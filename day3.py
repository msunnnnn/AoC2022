from aocd import data


input = data.splitlines()

# converting letters to unicode, use ord()
# https://www.delftstack.com/howto/python/convert-letter-to-number-python/

# Capital Letters -> (ord("A") - 38)
# Lower Case -> (ord("a")- 96)


def find_same_item(bags):

    total = 0
    for bag in bags:
        halfway = int(len(bag)/2)
        first = bag[slice(halfway)]
        last = bag[slice(halfway, len(bag))]
        for letter in first:
            if last.find(letter) != -1 :
                if letter.islower():
                    total += (ord(letter)- 96)
                elif not letter.islower():
                    total += (ord(letter) - 38)
                break

    return total




print(find_same_item(input))