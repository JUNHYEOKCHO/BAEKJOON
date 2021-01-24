N = int(input())

rope = []

for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(1, N+1):
    rope[i-1] = rope[i-1] * i

print(max(rope))
