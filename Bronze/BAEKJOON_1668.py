N = int(input())

trophy = []

for i in range(N):
    trophy.append(int(input()))

left = 1
right = 1

left_idx = trophy[0]
right_idx = trophy[-1]

for i in range(1, N):
    if trophy[i] > left_idx:
        left += 1
        left_idx = trophy[i]

    if trophy[-(i+1)] > right_idx:
        right += 1
        right_idx = trophy[-(i+1)]

print(left)
print(right)
