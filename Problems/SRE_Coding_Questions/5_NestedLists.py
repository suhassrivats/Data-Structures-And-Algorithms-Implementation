# Write a program that returns a list of sums of all sublists
def sublist_sum(data):
    output = []
    for l in data:
        output.append(sum(l))
    print(output)
    return output


# Write a function that accepts data and a target number. Print the first item
# which sum is greater than target or print that there is no such item
def greater_than_target(data, num):
    for l in data:
        if sum(l) > num:
            print(l)
            return l
    print('No sublist sum is greater than the target number')
    return None


# Return the first item containing 2 sequential items which sum is equal to
# target or None
def sequential2(data, num):
    for l in data:
        p1 = 0
        for p2 in range(1, len(l)):
            if num == l[p1] + l[p2]:
                print(l)
                return l
            p1 += 1
    return None


if __name__ == '__main__':
    # Input
    data = [[8, 3], [9, 1, 0], [5, 7, 12], [11, 6], [1, 4], [13], [9, 5, 6]]

    # Invoke function calls
    sublist_sum(data)
    greater_than_target(data, 15)
    sequential2(data, 10)
