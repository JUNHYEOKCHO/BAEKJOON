ascending = True
descending = True

results = list(map(int, input().split(" ")))

for i in range(len(results)-1):
    if results[i] > results[i+1]:
        ascending=False
    elif results[i] < results[i+1]:
        descending=False
        
if ascending:
    print('ascending')
elif descending:
    print("descending")
else:
    print("mixed")
