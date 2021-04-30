n = int(input())

answer = []

for _ in range(n):
    age, name = input().split(" ")
    answer.append((int(age), name))
    
answer_sorted = sorted(answer, key=lambda x: x[0])

for (age, name) in answer_sorted:
    print(f"{age} {name}")
