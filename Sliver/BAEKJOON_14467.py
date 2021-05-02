N =int(input())

moving_list = []

for _ in range(N):
    i, j = map(int, input().split(" "))

    moving_list.append((i, j))


moving_dict = {}
count = 0

for i, j in moving_list:
    if i in moving_dict.keys():
        if moving_dict[i] == j:
            continue
        else:
            moving_dict[i] = j
            count += 1
    else:
        moving_dict[i] = j

print(count)
        
