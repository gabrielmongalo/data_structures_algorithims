# What is the max n-steps it will take to get through a sorted list of 128 items
# using binary_search.

def binary_search(random_num_list, item):
    low = 0
    high = len(num_list)-1

    counter = 0

    while low <= high:
        mid = (low + high) / 2
        guess = num_list[mid]
        counter += 1

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return None
    return counter


num_list = list(range(0,128))

print(num_list)
print('List size is' + ' '+ str(len(num_list)))

print(binary_search(num_list, num_list[-1:]))
print(binary_search(num_list*2, num_list[-1:]))
