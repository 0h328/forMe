import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    my_list = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        tmp = my_list[i-2]
        tmp2 = my_list[i-2]
        for j in range(-2, 3):
            if my_list[i+j] > tmp:
                tmp = my_list[i+j]
        for k in range(-2, 3):
            if tmp2 < my_list[i+k] < tmp:
                tmp2 = my_list[i+k]
        if my_list[i] == tmp:
            my_view = tmp - tmp2
            total += my_view
    print('#{} {}'.format(test_case, total))

# 테스트 케이스 1번만 맞고 나머지는 값이 다르게 나오는데 아직 이유를 파악하지 못했다.