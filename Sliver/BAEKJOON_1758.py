N = int(input())

array = []

for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

tip = 0

for i, value in enumerate(array):
    t = value - i

    if t <= 0:
        continue

    tip += t

print(tip)
