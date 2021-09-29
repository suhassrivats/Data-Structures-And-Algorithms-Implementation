"""
Combining two lists while removing duplicates in the new list and keeping
duplicates in original list returns a list of containing all of the values in
the first list and all unique values in the second that are not in the first.
For example, combining [1, 2, 2, 3,] and [3, 4] with these conditions will
return [1, 2, 2, 3, 4].
"""


def combined_duplicate_sets(list_1, list_2):
    set1 = set(list_1)
    set2 = set(list_2)

    set2_without_set1_items = list(set2-set1)
    combined_list = list_1 + set2_without_set1_items

    print(combined_list)
    return combined_list


def main():
    list_1 = [1, 2, 2, 3]
    list_2 = [3, 4]
    combined_duplicate_sets(list_1, list_2)


if __name__ == '__main__':
    main()
