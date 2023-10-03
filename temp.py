MOD = 10**9 + 7

def solve(n,s):
    dp = [[0]*(n/2+1) for _ in range(n//2+1)]

    for i in range(n//2+1):
        dp[i][0]=1
    
    for i in range(1,n//2+1):
        for j in range(1,i+1):
            dp[i][j] = (dp[i-1][j]+dp[i-1][j-1])%MOD

    result = sum(dp[n//2]) %MOD

    return result

t = 1
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    result = solve(n,s)
    print(result)