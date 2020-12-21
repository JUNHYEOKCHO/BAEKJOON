n = int(input())

a1, a2 = 0, 1

while n > 0:
    a1, a2 = a2, a1 + a2

    n -= 1

print(a1)
