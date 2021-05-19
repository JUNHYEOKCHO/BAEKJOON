L, P = list(map(int, input().split(" ")))

A = list(map(int, input().split(" ")))

T = L * P

A = [str(a - T) for a in A]

print("".join(A))
