def fibo_dp(num):
    # 일단 크기만큼의 0으로 이루어진 배열 생성
    cache = [0 for _ in range(num+1)]

    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index-1] + cache[index-2]

    return cache[num]


print(fibo_dp(100))
