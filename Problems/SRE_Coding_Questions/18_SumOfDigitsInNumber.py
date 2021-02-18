def sum_of_digits_in_number(num):
    return sum([int(dig) for dig in str(num)])


def sum_of_digits_in_number_regular(num):
    total = 0
    while num != 0:
        total += num % 10
        num = num//10
    print(total)
    return total


# sum_of_digits_in_number(123456)
sum_of_digits_in_number_regular(12345)
