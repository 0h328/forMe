import sys
sys.stdin = open('input.txt')























# def put_a_paper(k):
#     if k == 1:  # 첫번째 idx 1은 1
#         return 1
#     if k == 2:  # 두번째 idx 2는 3
#         return 3
#
#     return put_a_paper(k - 1) + 2 * put_a_paper(k - 2)  # 점화식
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     k = N / 10  # 10의 배수이기 때문에, 10으로 나눠서 풀이
#
#     print("#{} {}".format(tc, put_a_paper(k)))