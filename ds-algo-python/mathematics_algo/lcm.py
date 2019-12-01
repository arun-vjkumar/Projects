from mathematics_algo.gcd import get_gcd


def get_lcm(num1: int, num2: int) -> int:
    return int((num1 * num2) / get_gcd(num1=num1, num2=num2))


if __name__ == '__main__':
    print(get_lcm(15, 20))

    arr = [2, 7, 3, 9, 4]

    lcm = None
    multiple_val = 0
    for i in range(0, len(arr) - 1):
        if lcm is None:
            lcm = get_lcm(arr[i], arr[i + 1])
        else:
            lcm = get_lcm(lcm, arr[i + 1])

    print(lcm)

