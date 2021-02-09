def binary_search(data, search):
    # 절반씩절반씩 짜르다가 마지막 한개에 도달하게 됨.
    # 그럼에도 0번에 있는게 내가 search 하고자 하는 데이터라면?
    if len(data) == 1 and search == data[0]:
        return True
    # 마지막께 내가 찾는게 아니라면?
    if len(data) == 1 and search != data[0]:
        return False
    # 데이터가 없으면
    if len(data) == 0:
        return False

    # 데이터 길이의 몫
    medium = len(data) // 2

    if search == data[medium]:
        return True
    else:
        # 찾는 데이터가 중앙값보다 크다면?
        if search > data[medium]:
            # 뒷단의 리스트로 이진탐색
            return binary_search(data[medium:], search)
        # 찾는 데이터가 중앙값보다 작다면?
        else:
            # 앞단의 리스트로 이진탐색
            return binary_search(data[:medium], search)
