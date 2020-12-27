N = int(input())


song = 1
count = 0

while N != 0:
    if N < song:
        song = 1
    else:
        N -= song
        count += 1
        song += 1

print(count)
        
