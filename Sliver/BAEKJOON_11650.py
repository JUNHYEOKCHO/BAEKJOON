n = int(input())
position = []

for _ in range(n):
    x, y = list(map(int, input().split(" ")))
    position.append((x, y))

position.sort()

for (i, j) in position:
    print(f"{i} {j}")
