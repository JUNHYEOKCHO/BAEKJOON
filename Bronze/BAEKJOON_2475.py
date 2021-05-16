a = list(map(int, input().split(" ")))

total = 0

for t in a:
    total += t*t
    
print(total % 10)
