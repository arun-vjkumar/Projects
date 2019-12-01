def get_bin_diff(n1: int, n2: int) -> bin:
    return sum([int(b) for b in str(bin(n2 ^ n1)) if b == '1'])


if __name__ == '__main__':
    n = 4
    arr = [(1, 1), (1, 3), (1, 5), (3, 1), (3, 3), (3, 5), (5, 1), (5, 3), (5, 5)]
    diff = 0
    for n1, n2 in arr:
        diff += get_bin_diff(n1, n2)
    print(diff)
