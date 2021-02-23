def find_largest_palindrome() -> int:
    max_palindrom = 0
    for i in range(999, 10, -1):
        for j in range(999, 10, -1):
            prod = i * j
            if is_palindrom(prod):
                if prod > max_palindrom:
                    max_palindrom = prod
    return max_palindrom


def is_palindrom(num):
    num_as_str = str(num)
    for i in range(int(len(num_as_str)/2)):
        if num_as_str[i] != num_as_str[-1-i]:
            return False
    return True


# Example:
# 99 * 91
# 9009
if __name__ == '__main__':
    print(find_largest_palindrome())
