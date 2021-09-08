def count_factorial_trailing_zeroes(num):
    """This function counts amount of trailing zeroes in a decimal representation of a factorial of given number
    :param num:
    :return:
    """
    res = 0
    while num >= 5:
        res += num // 5
        num //= 5
    return res


if __name__ == '__main__':
    print(count_factorial_trailing_zeroes(int(input())))
