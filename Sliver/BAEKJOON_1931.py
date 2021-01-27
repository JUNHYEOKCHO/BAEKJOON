import heapq

N = int(input())

array = []

length = 0
last = 0

for _ in range(N):
    a, b = map(int, input().split(" "))

    array.append((a, b))

array = sorted(array, key=lambda x : x[0])

array = sorted(array, key=lambda x : x[1])

for i, j in array:
    if i >= last:
        last = j

        length += 1

print(length)

