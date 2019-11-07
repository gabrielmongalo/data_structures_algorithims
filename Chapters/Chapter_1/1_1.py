from typing import List, Union

# What is the max n-steps it will take to get through a sorted list of 128 items
# using binary_search.

def binary_search(num_list: List, item: int) -> Union[int, None]:
    low = 0
    high = len(num_list)-1

    counter = 0

    while low <= high:
        mid = (low + high) // 2
        guess = num_list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return None

        counter += 1

    return counter


num_list = range(0,127)
num_list_doubled = range(0,255)

print(f'''Max number of steps for 128 items {binary_search(num_list, 127)}''')
print(f'''Max number of steps for 256 items {binary_search(num_list_doubled, 255)}''')
