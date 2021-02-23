
def find_fibonacci_even_sum(max_num) -> int:
    even_sum = 2
    fib_num1 = 1
    fib_num2 = 2
    while fib_num2 < max_num:
        tmp = fib_num2
        fib_num2 += fib_num1
        if fib_num2 % 2 == 0:
            even_sum += fib_num2
        fib_num1 = tmp
    return even_sum


if __name__ == '__main__':
    max_num = 4000000
    print(find_fibonacci_even_sum(max_num))
