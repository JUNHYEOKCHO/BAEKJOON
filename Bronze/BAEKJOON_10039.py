score = []

for i in range(5):
    score.append(int(input()))

total = 0

for s in score:
    if s < 40:
        total += 40
        continue

    total += s

print(int(total/5))
