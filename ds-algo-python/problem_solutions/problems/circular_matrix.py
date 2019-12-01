
def print_circular_matrix(n: int) -> None:
    sum = 0
    if n % 2 != 0:
        for i in range(1, (n * n) + 1):
            if i % 2 != 0:
                sum += i
            else:
                print("How do i know")
    print(sum)


if __name__ == '__main__':
    print_circular_matrix(3)

# [34, 33, 32, 31, 30,29]
# [35, 16, 15, 14, 13, 28]
# [36, 17, 5, 4, 3, 12, 27]
# [37, 18, 6, 1, 2, 11, 26]
# [38, 19, 7, 8, 9, 10, 25]
# [39, 20, 21, 22, 23, 24]
