def addBinary(a, b):
    carry = 0
    result = ''
    # convert string inputs to lists
    # so a = "1010", b = "1011" become
    # a = ['1', '0', '1', '0']
    # b = ['1', '0', '1', '1']
    a = list(a)
    b = list(b)

    # iterate thru the lists if there any value in a or b or carryover is 1
    # then keep looping
    while a or b or carry:
        if a:
            # remove the last item from the list
            # convert string to integer so we can do arithmetic
            # e.g. carry += int('0') - for the first iteration
            carry += int(a.pop())
        if b:
            # e.g. carry += int('1') - for the first iteration
            carry += int(b.pop())

        # we need only 1 and 0 so use modulo 2
        # e.g. if carry is 2, then 2 % 2 = 0
        # then convert it to string and store in result
        result += str(carry % 2)

        # do division to get the quotient
        # e.g. 2 // 2 = 1 so the carryover is 1 which need to take
        # in to account for the next iteration

        carry //= 2
    # lastly, i just return the reverse of the result
    # e.g. result = '10' -> '01'
    return result[::-1]


# Tests
a = "11"
b = "1"
print(addBinary(a, b))
