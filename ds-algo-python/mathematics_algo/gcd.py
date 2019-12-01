def get_gcd(num1: int, num2: int) -> int:
    if num1 == 0:
        return num2
    return get_gcd(num2 % num1, num1)


def reduce_number(num1: int, num2: str) -> int:
    mod = 0
    for i in range(len(num2)):
        mod = (mod * 10 + int(num2[i])) % num1
    return mod


def handling_gcd_for_big_numbers(num1: int, num2: str) -> int:
    new_num = reduce_number(num1, num2)
    return get_gcd(num1, new_num)


if __name__ == '__main__':
    print(get_gcd(8, 12))

    arr = [2, 4, 6, 8, 16]
    gcd = None
    for i in range(0, len(arr) - 1):
        if gcd is None:
            gcd = get_gcd(arr[i], arr[i + 1])
        else:
            gcd = get_gcd(gcd, arr[i + 1])
    print(gcd)

    num1 = 1221
    num2_str = "1234567891011121314151617181920212223242526272829"
    print(handling_gcd_for_big_numbers(num1, num2_str))

