import sys
input = sys.stdin.readline
n = int(input())
checkPoint = [list(map(int, input().split())) for _ in range(n)]
allDis = []
def calcDis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

total = 0
for i in range(n - 1):
    dis = calcDis(checkPoint[i], checkPoint[i + 1])
    allDis.append(dis)
    total += dis

ans = int(1e9)
for i in range(1, n - 1):
    temp = total - allDis[i] - allDis[i - 1] + calcDis(checkPoint[i - 1], checkPoint[i + 1])
    ans = min(temp, ans)

print(ans)