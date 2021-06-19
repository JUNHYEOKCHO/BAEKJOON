M, N, A = map(int,input().split(" "))

price = M * N - A

if price > 0:
    print(price)
else:
    print(0)
