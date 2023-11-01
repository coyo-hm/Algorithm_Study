import sys
input = sys.stdin.readline
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(N):
    w, h = info[i]
    rank = 1
    for j in range(N):
        if i == j:
            continue
        elif w < info[j][0] and h < info[j][1]:
            rank += 1
    answer.append(str(rank))

print(" ".join(answer))