import sys
sys.stdin = open('input.txt')

# 1. 숫자
num = int(input())
print(num)

# 2. 리스트
nums = list(map(int, input().split()))
print(nums)

# for num in nums:
#     print(num)

# 3. 이차원 리스트
N = int(input())

# my_nums = []
# for _ in range(N):
#     nums = list(map(int, input().split()))
#     my_nums.append(nums)
# print(my_nums)

# 조금 더 심플한 버전
numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)