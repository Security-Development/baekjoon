"""
부분수열: 주어진 수열에서 몇 개의 항을 순서를 유지한 채로 몇몇 항들을 제외하여 얻은 수열
순증가수열: 현재 항이 이전의 항 보다 같아도 안되고 무조건 커야하는 조건이 성립되는 수열
"""

def int_input():
    return int(input(), 10)

def list_input():
    return list(map(int, input().split()))

N = int_input()
S = list_input()
M = int_input() 
A = list_input()

dp = [[[0, (-1, -1)] for _ in range(N)] for _ in range(M)]

def lcs(a=0, b=0):
    if a == N - 1:
        return

    if b == M - 1:
        lcs(a + 1, 0)
        return
    
    if S[a] == A[b]:
        dp[a][b][0] += 1

        for k in range(a+1, N):
            if S[k] <= S[a]:
                continue
            for l in range(b+1, M):
                if A[l] == S[k] and dp[k][l][0] < dp[a][k][0]:
                    dp[k][l] = [dp[a][k][0], (a, b)]
                    break
    
    lcs(a, b + 1)

    max_value = -float('inf')
    max_position = None

    for i in range(M):
        for j in range(N):
            current_value = dp[i][j][0]
            if current_value > max_value:
                max_value = current_value
                max_position = (i, j)
    
    return max_value, max_position

lcs_value, position = lcs()
x, y = position

subsquence = []
while x != y and x != -1:
    subsquence.insert(0, S[x])
    x, y = dp[x][y][1]

print(lcs_value)
print(*subsquence)
