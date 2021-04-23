n = int(input())

answer = []
for _ in range(n):
    answer.append(int(input()))

answer.sort()

for i in answer:
    print(i)
