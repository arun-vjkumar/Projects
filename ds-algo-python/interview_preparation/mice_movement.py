def mice(A, B):
    max_diff = 0
    A = sorted(A)
    B = sorted(B)

    for i in range(len(A)):
        if A[i] < 0 and B[i] < 0:
            diff = abs(A[i] - B[i])
        elif A[i] < 0 or B[i] < 0:
            diff = abs(A[i] - B[i]) if A[i] < 0 else abs(B[i] - A[i])
        else:
            diff = abs(A[i] - B[i])
        print(A[i], B[i], diff)

        if max_diff < diff:
            max_diff = diff

    return max_diff


if __name__ == '__main__':
    A = [-49, 58, 72, -78, 9, 65, -42, -3 ]
    B = [30, -13, -70, 58, -34, 79, -36, 27]
    print(mice(A, B))