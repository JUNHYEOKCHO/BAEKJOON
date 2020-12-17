from itertools import combinations

N, M = list(map(int, input().split(" ")))

cards = list(map(int, input().split(" ")))

result = -1

for i, j, k in combinations(cards, 3):
    value = i + j + k

    if value <= M:
        if value >= result:
            result = value

        if value == M:
            break

print(result)
