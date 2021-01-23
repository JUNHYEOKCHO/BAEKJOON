N = int(input())
time = list(map(int, input().split(" ")))

time.sort()

cumul = []

for t in time:
    try:
        k = t + cumul[-1]
        cumul.append(k)
    except:
        cumul.append(t)

print(sum(cumul))
