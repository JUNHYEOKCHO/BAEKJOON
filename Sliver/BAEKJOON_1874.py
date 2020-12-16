# n 입력
n = int(input())

# 숫자 세기를 위한 count 변수
count  = 1

# 숫자를 담기 위한 stack1, +-를 담기 위한 stack2
stack1 = []
stack2 = []

# 반복문을 통해 n번만큼 실행
for i in range(n):
    # 숫자 입력
    num = int(input())
    
    # count가 입력받은 숫자보다 작다면 stack1에 숫자를 담고 stack2에 +를 담는다.
    while count <= num:
        stack1.append(count)
        stack2.append('+')
        count += 1
    
    # stack1에 들어있는 마지막 원소가 입력받은 숫자와 같다면 내보내고 stack2에 -를 담기
    if stack1[-1] == num:
        stack1.pop()
        stack2.append('-')
    # 차순 정렬이 안된다면 프로그램 종료시키기
    else:
        print('NO')
        exit(0)

# 결과 출력
print("\n".join(stack2))
