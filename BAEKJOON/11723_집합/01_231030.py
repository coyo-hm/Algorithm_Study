import sys
input = sys.stdin.readline
M = int(input())
S = [0] * 21

for _ in range(M):
    exp = input().split()
    if exp[0] == "add":
        x = int(exp[1])
        if S[x] == 0:
            S[x] = 1
    elif exp[0] == "remove":
        x = int(exp[1])
        S[x] = 0
    elif exp[0] == "check":
        x = int(exp[1])
        print(S[x])
    elif exp[0] == "toggle":
        x = int(exp[1])
        if S[x] == 1:
            S[x] = 0
        else:
            S[x] = 1
    elif exp[0] == "all":
        S = [1] * 21
    elif exp[0] == "empty":
        S = [0] * 21

