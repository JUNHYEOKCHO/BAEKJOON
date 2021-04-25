test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(" ")))
    queue = list(map(int, input().split(" ")))
    
    count = 1
    
    queue = [(val, idx) for idx, val in enumerate(queue)]
    
    while True:
        if queue[0][0] == max(queue, key=lambda x : x[0])[0]:
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
                count += 1
        else:
            queue.append(queue.pop(0))
