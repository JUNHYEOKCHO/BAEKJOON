import heapq

N = int(input())

array = []

q = []

for _ in range(N):
    a, b = map(int, input().split(" "))

    array.append((a, b))

array.sort()

for i, j in array:
    heapq.heappush(q, j)

    if len(q) > i:
        heapq.heappop(q)

print(sum(q))
