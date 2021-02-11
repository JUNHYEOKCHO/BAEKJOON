# 파이썬으로 그래프를 표현하는 방법은 딕셔너리와 리스트 자료 구조를 활용하여 표현 가능

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    # 방문한 queue
    visited = list()
    # 방문이 필요한 queue
    need_visit = list()

    # 어떤 노드부터 시작할지 큐에 담아놓고 시작
    need_visit.append(start_node)

    # 더 이상 방문할 노드가 없다면 종료
    while need_visit:
        # 그냥 팝하면 맨 마지막께 뽑힘.
        # 숫자를 넣어주면 해당 인덱스가 뽑혀져 나옴
        node = need_visit.pop(0)

        # 만약에 뽑아온 노드가 visited 큐에 없으면?
        if node not in visited:
            # 방문한 큐에 더해주고
            visited.append(node)
            # 방문 해야할 노드를 해당 노드와 연결된 친구들을 더해줌
            need_visit.extend(graph[node])

    return visited

print(bfs(graph, 'A'))
