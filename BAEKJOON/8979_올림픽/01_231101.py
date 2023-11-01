import sys
input = sys.stdin.readline
N, K = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
countries.sort(key=lambda x:(-x[1], -x[2], -x[3]))
rank = 1

for i in range(N):
    if i > 0 and countries[i][1:] != countries[i - 1][1:]:
        rank = i + 1
    if countries[i][0] == K:
        break

print(rank)