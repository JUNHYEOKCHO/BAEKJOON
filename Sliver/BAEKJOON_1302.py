n = int(input())

book_dic = {}

for i in range(n):
    name = input()

    if name not in book_dic.keys():
        book_dic[name] = 1
    else:
        book_dic[name] += 1


target = max(book_dic.values())
array = []

for book, number in book_dic.items():
    if number == target:
        array.append(book)

print(sorted(array)[0])
