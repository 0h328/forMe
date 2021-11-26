def solve_while(target, pattern, N, M):
    i = 0
    j = 0
    while j < M and i <N:
        if target[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i-j
    else:
        return 0

def solve_for(target, pattern, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if target[i+j] != pattern[j]:
                break
            elif j==M-1:
                return i



import sys
sys.stdin = open('input.txt')
target = input()
N = len(target)

pattern = input()
M = len(pattern)


# 방법 1 - while
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans = solve_while(target, pattern, N, M)
print('{}'.format(ans))		# 2

# 방법 2 - for
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans2 = solve_for(target, pattern, N, M)
print('{}'.format(ans2))	# 2

# 방법 3 - .find() 활용
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
print(target.find(pattern)) # 2