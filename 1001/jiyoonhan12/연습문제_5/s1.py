"""
연습문제 5. 부분 집합 구현

5-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def powerset(N):
    for i in range((1 << N)):
        for j in range(N):
            if i & (1 << j):
                print('%d' %nums[j], end=' ')
        print()

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
powerset(N)

"""
-1 3 -9 6 7 -6 1 5 4 -2 
-1 3 -9 6 7 -6 1 5 4 
-1 3 -9 6 7 -6 1 5 -2 
-1 3 -9 6 7 -6 1 5 
-1 3 -9 6 7 -6 1 4 -2 
-1 3 -9 6 7 -6 1 4 
-1 3 -9 6 7 -6 1 -2 
-1 3 -9 6 7 -6 1 
-1 3 -9 6 7 -6 5 4 -2 
-1 3 -9 6 7 -6 5 4 
-1 3 -9 6 7 -6 5 -2 
-1 3 -9 6 7 -6 5 
-1 3 -9 6 7 -6 4 -2 
...
"""