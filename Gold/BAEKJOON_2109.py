import heapq

N = int(input())

array = []

q = []

for _ in range(N):
    a, b = map(int, input().split(" "))

    array.append((a, b))

array = sorted(array, key = lambda x: x[1])

for i, j in array:
    heapq.heappush(q, i)

    if len(q) > j:
        heapq.heappop(q)

print(sum(q))
