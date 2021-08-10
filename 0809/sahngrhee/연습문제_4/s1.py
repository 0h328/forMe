import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    c = [0] * 12

    for i in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(test_case, ans))