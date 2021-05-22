a = [1, 1, 2, 2, 2, 8]

b = list(map(int, input().split(" ")))

c = []

for i in range(len(a)):
    c.append(str(a[i] - b[i]))
    
print(" ".join(c))
    
