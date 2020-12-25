N = int(input())

num_list = []


[num_list.append(int(input())) for _ in range(N)]


num_list.sort()

for data in num_list:
    print(data)
