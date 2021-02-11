# 랜덤 데이터 탐
from random import *

rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1, 100))

print(rand_data_list)

def sequential(data_list, search_data):4
    # 데이터의 길이만큼 반복
    for index in range(len(data_list)):
        # matching이 일어날시 index 반
        if data_list[index] == search_data:
            return index

    return -1

