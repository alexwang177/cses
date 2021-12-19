import sys


def rca():
    return list(sys.stdin.readline().strip())


A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
MAX = (10**9)+7

dp = [[MAX for _ in range(len(B) + 1)]
      for _ in range(len(A) + 1)]

dp[0][0] = 0

for i in range(len(A) + 1):

    for j in range(len(B) + 1):

        a = dp[i-1][j] + 1 if i > 0 else MAX
        b = dp[i][j-1] + 1 if j > 0 else MAX
        c = dp[i-1][j-1] + (0 if A[i-1] == B[j-1]
                            else 1) if i > 0 and j > 0 else MAX

        # dp[i][j] = min(dp[i][j], a, b, c)
        dp[i][j] = min(dp[i][j], a, b, c)

# print(dp)
ans = dp[len(A)][len(B)]
print(ans)

'''
        i

    0 1 2 3
A:  L O V E 
   
          j

    0 1 2 3 4
B:  M O V I E

dp[i][j] = min distance for strings A[0...i-1] and B[0...j-1]

dp[i][j] = min ( 

    dp[i-1][j-1] -> A[i-1] = B[j-1]
    
    dp[i-1][j-1] + 1 -> replace A[i-1] with B[j-1]

    dp[i][j-1] + 1 -> add B[j-1] at A[i]

    dp[i-1][j] + 1 -> delete A[i-1]

    )
'''
