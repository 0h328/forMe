import sys

sys.stdin = open('input.txt')


def ladder_lottery(lst):

    for c in range(100):

        r = 0

        if ladder_list[r][c] == 1:
            start_c = c
            chk = 0

            while r < 100:
                if ladder_list[r][c] == 2:
                    return start_c

                if c - 1 >= 0:
                    if ladder_list[r][c - 1] == 1 and (chk == 0 or chk == 1):
                        c = c - 1
                        chk = 1
                        continue

                if c + 1 < 100:
                    if ladder_list[r][c + 1] == 1 and (chk == 0 or chk == 2):
                        c = c + 1
                        chk = 2
                        continue
                chk = 0
                r += 1


idx = 1

while idx <= 10:
    test_num = int(input())

    ladder_list = [list(map(int,input().split())) for _ in range(100)]

    print('#{0} {1}'.format(idx, ladder_lottery(ladder_list)))

    idx += 1
