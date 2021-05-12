time = []

for _ in range(4):
    time.append(int(input()))

t, m = divmod(sum(time), 60)

print(t)
print(m)
