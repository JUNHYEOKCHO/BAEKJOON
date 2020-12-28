n = input()

m = input()


idx = 0
count = 0

while idx + len(m) - 1 < len(n):
    if n[idx] == m[0]:

        print("\n %s, %s \n" %(n[idx], m[0]))
        
        if n[idx:idx+len(m)] == m:
            count += 1
            idx += len(m)

    else:
        idx += 1
print(count)
