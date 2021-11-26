"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = 1
            print('방문정점:{}, 방문체크:{}'.format(v, visited))

            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

for i in range(E):
    G[temp[i * 2]][temp[i * 2 + 1]] = 1
    G[temp[i * 2 + 1]][temp[i * 2]] = 1
# 인접리스트
# G = [[] for _ in range(V + 1)]
# print(G)
#
# for i in range(1, len(temp), 2):
#     G[temp[i-1]].append(temp[i])
#     G[temp[i]].append(temp[i-1])
# 방문 표시 초기화
visited = [0 for _ in range(V + 1)]

# dfs 탐색 시작
dfs(1)