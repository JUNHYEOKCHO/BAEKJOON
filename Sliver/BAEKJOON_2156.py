n = int(input())

wine = [int(input()) for x in range(n)]

drink = [0]

# 첫 잔 일단 추가
drink.append(wine[0])

# n이 1보다 크변 2번째 잔까지 마신 값 일단 추가
if n > 1:
    drink.append(wine[0] + wine[1])

# 연속 3잔은 못마심
for i in range(3, n+1):
    # 이번 포도주 먹고 이전 포도주 안먹은 경우
    case1 = wine[i-1] + drink[i-2]

    # 이번 포도주 먹고 다음 포도주도 먹음
    case2 = wine[i-1] + wine[i-2] + drink[i-3]

    # 이번 포도주는 못먹음
    case3 = drink[i-1]

    # 가장 큰 값을 주는 경우로 설정
    max_value = max(case1, case2, case3)

    drink.append(max_value)

print(drink[n])
