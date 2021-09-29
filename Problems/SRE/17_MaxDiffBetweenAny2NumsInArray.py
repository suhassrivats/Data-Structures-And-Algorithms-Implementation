def max_abs_diff(arr):
    # Maximum difference is the absolute diff between max and min element

    min_element = float('inf')
    max_element = float('-inf')

    for num in arr:
        min_element = min(min_element, num)
        max_element = max(max_element, num)

    print(max_element - min_element)
    return (max_element - min_element)


def stocks_max_profit(arr):
    min_price = arr[0]
    max_cost = 0

    for num in arr:
        min_price = min(min_price, num)
        cost = num - min_price
        max_cost = max(max_cost, cost)

    print(max_cost)
    return max_cost


def main():
    # arr = [2, 1, 5, 3, -10]
    arr = [7, 1, 5, 3, 6, 4]
    # max_abs_diff(arr)
    stocks_max_profit(arr)


if __name__ == '__main__':
    main()
