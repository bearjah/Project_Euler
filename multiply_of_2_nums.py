def multiply_of_2_nums(num1, num2, n):
    sum_result = 0
    for i in range(min(num1, num2), n):
        if (i % num1) == 0 or (i % num2) == 0:
            sum_result += i
            # print(i)
    return sum_result


if __name__ == '__main__':
    num1 = 3
    num2 = 5
    n = 1000
    print(multiply_of_2_nums(num1, num2, n))
