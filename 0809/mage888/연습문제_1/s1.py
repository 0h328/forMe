import sys
sys.stdin = open('input.txt')

#1. 숫자
# T = int(input())
N = int(input())
print(N)
# print(num)
# print('#{}'.format(num))

#2. 리스트
print(input())
print(input().split())
print([0] + list(map(int, input().split())))
# nums = list(map(int, input().split()))
# #
# for num in nums:
#     print(num)

#3. 이차원 리스트
# N = int(input())
#
# my_nums = []
# for _ in range(N):
#     nums = list(map(int, input().split()))
#     print(nums)
#     my_nums.append(nums)
# print(my_nums)

#조금 더 심플한 버전
# numbers = [list(map(int, input().split())) for _ in range(N)]
# print(numbers)