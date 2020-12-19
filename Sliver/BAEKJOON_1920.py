n = int(input())
A = set(map(int, input().split(" ")))
m = int(input())
nums = list(map(int, input().split(" ")))

for i in nums:
    if i in A:
        print(1)
    else:
        print(0)
