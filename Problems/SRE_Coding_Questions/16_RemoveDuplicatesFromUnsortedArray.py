# Using Hashmap/dictionary
def remove_duplicates_unsorted_arr(input):
    num_freq_map = {}

    # Add all nums to dictionary with value 0
    for num in input:
        num_freq_map[num] = num_freq_map.get(num, 0)

    # Once a number is printed, update dictionary with any value other than 0
    for num in input:
        if num_freq_map[num] == 0:
            print(num, end=' ')
            num_freq_map[num] = 1


# Using set
def remove_duplicates_unsorted_arr(input):
    return list(set(input))


input = [1, 2, 5, 1, 7, 2, 4, 2]
remove_duplicates_unsorted_arr(input)
