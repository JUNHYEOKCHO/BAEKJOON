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

# need_visit을 stack, visted를 queue로 짜면 DFS 구현 가능
# stack이니까 뒤에 있는 데이터 먼저 탐지
def dfs(graph, start_node):
    visited, need_visit = list(), list()

    need_visit.append(start_node)

    while need_visit:
        # 그냥 pop을 하면 맨 뒤의 원소를 그냥 꺼내오게 된다.
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

print(dfs(graph, 'A'))
