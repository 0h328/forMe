import sys
sys.stdin = open('input.txt')
from collections import deque


def select_position(i, removed_cnt):
    global res
    if i <= n:
        if res < removed_cnt:
            res = removed_cnt

        for j in range(w):
            if 0 in status[j]:
                changed = remove_blocks(j)
                for x, y in changed:
                    status[x][y] = 1
                select_position(i + 1, removed_cnt + len(changed))
                recover_blocks(changed)


def find_block(col, s, e, order):
    c = 0
    for i in range(s, e, -1 if s > e else 1):
        if status[col][i] != 1:
            c += 1
            if c == order:
                return i
    return -1


def remove_blocks(column_idx): #bfs
    global status
    changed = set()
    visited = [[0] * h for _ in range(w)]
    q = deque([(column_idx, find_block(column_idx, lengths[column_idx]-1, -1, 1))])
    changed.add((q[0][0], q[0][1]))
    visited[q[0][0]][q[0][1]] = 1

    while q:
        x, y = q.popleft()
        if l[x][y] == 1:
            continue
        order = status[x][:y+1].count(0)
        # 가로
        for j in range(max(x - l[x][y] + 1, 0), min(w, x + l[x][y])):
            if j == x:
                continue
            k = find_block(j, 0, lengths[j], order)
            if k != -1 and visited[j][k] == 0:
                visited[j][k] = 1
                changed.add((j, k))
                q.append((j, k))
        # 세로
        c = 1
        for k in range(y - 1, -1, -1):
            if status[x][k] == 0 and visited[x][k] == 0:
                c += 1
                visited[x][k] = 1
                changed.add((x, k))
                q.append((x, k))
                if c == l[x][y]:
                    break
        c = 1
        for k in range(y + 1, lengths[x]):
            if status[x][k] == 0 and visited[x][k] == 0:
                c += 1
                visited[x][k] = 1
                changed.add((x, k))
                q.append((x, k))
                if c == l[x][y]:
                    break
    return changed

def recover_blocks(changed_list):
    for i, j in changed_list:
        status[i][j] = 0

t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for idx in range(1, t+1):
    n, w, h = map(int, input().split())
    l = list(map(lambda x: list(filter(lambda x: x != 0, list(x)[::-1])), zip(*[list(map(int, input().split())) for _ in range(h)])))
    lengths = [len(l[i]) for i in range(w)]
    status = [[0] * lengths[i] for i in range(w)]
    res = 0

    select_position(0, 0)
    print('#{} {}'.format(idx, sum(lengths) - res))