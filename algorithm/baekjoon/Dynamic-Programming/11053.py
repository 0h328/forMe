N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
# i = 1 1,2,1,1,1,1
# i = 2 1,2,1,1,1,1
# i = 3 1,2,1,2,1,1
# i = 3 1,2,1,3,1,1
# i = 3 1,2,1,3,1,1
# i = 4 1,2,1,3,2,1
# i = 4 1,2,1,3,2,1
# i = 4 1,2,1,3,2,1
# i = 5 1,2,1,3,2,2
# i = 5 1,2,1,3,2,3
# i = 5 1,2,1,3,2,3
# i = 5 1,2,1,3,2,4

for i in range(1, N): # 1,2,3,4,5
    for j in range(i): # i=1,2,3,4,5,
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

