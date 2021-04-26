def get_square(N, board):
    # 해당 라인에 0이 없으면 1 추가해주기
    if not any(0 in x for x in board):
        square_count.append(1)
        return
    # 해당 라인에 0이 없으면 1 추가해주기
    elif not any(1 in x for x in board):
        square_count.append(0)
        return
    else:
        # 0을 세는 리스트
        count_0 = []
        # 1을 세는 리스트
        count_1 = []
        for i in board:
            # 2로 나눈 몫을 담기
            count_0.append(i[:N//2])
            count_1.append(i[N//2:])

        # 사이즈를 1/2 씩 줄여가며 재귀적으로 호출
        get_square(N//2, count_0[:N//2])
        get_square(N//2, count_0[N//2:])
        get_square(N//2, count_1[:N//2])
        get_square(N//2, count_1[N//2:])
        return
    


N = int(input())
board = []
square_count = []

# 보드 생성
for _ in range(N):
    line = list(map(int, input().split(" ")))
    board.append(line)

get_square(N, board)
print(square_count.count(0))
print(square_count.count(1))
