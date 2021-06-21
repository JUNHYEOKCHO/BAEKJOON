A, B, C = map(int, input().split(" "))





if B >= C:
    print(-1)
else:

    D = C - B

    count = A // D + 1

    print(count)

