N, K = list(map(int, input().split(" ")))

array = list(map(int, input().split(" ")))

array = sorted(array)
print(array[K-1])
