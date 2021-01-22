N, K = list(map(int, input().split(" ")))

coins = []

for _ in range(N):
    coins.append(int(input()))

count = 0

coins.reverse()

for coin in coins:
    if K // coin == 0:
        continue
    else:
        num = K // coin
        K = K % coin
        count += num

print(count)
