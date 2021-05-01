n = int(input())

a = list(map(int, input().split(" ")))

s = sorted(a)

s = [(value, index) for index, value in enumerate(s)]

answer = []
for i in range(len(a)):
    for j in range(len(s)):
        if s[j][0] == a[i]:
            answer.append(str(s[j][1]))
            s.pop(j)
            break
            
print(" ".join(answer))
