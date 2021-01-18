N = int(input())

rank = []
dis = 0

for i in range(N):
    rank.append(int(input()))

rank.sort()

for i in range(N):
    dis += abs(rank[i] - (i+1))

print(dis)
