def search(start):
    r = 99 # 목적지는 무조건 99번째 행에 있으므로 고정
    c = start

    while r > 0:            # 맨 윗줄에 도착하기 전까지 위로 올라감
        r -= 1              # 위로 한 칸 이동
        if c > 0 and a[r][c-1] == 1:            # 왼쪽으로 사다리를 안 벗어나고, 왼쪽 칸이 1이면
            while c > 0 and a[r][c-1] == 1:     # 사다리를 벗어나거나, 왼쪽이 1이 아닐때까지 while문 수행
                c -= 1
        elif c < 99 and a[r][c+1] == 1:         # 오른쪽으로 사다리를 안 벗어나고, 오른쪽 칸이 1이면
            while c < 99 and a[r][c+1] == 1:    # 사다리를 벗어나거나 오른쪽이 1이 아닐때까지 while문 수행
                c += 1

    return c

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(100)]

    for c in range(100):
        if a[99][c] == 2:
            break

    # print(c)

    ans = search(c)

    print('#{} {}'.format(tc, ans))


