n = input()

count0 = 0
count1 = 0

if n[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if n[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
