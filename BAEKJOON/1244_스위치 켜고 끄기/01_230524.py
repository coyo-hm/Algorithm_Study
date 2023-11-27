import sys

input = sys.stdin.readline

switchNum = int(input())
switchList = list(map(int, input().split()))
stdNum = int(input())


def calcOne(s):
    for i in range(switchNum // s):
        switchList[(i + 1) * s - 1] = (switchList[(i + 1) * s - 1] + 1) % 2


def calcTwo(s):
    switchList[s] = (switchList[s] + 1) % 2
    for i in range(1, switchNum):
        if s - i < 0 or s + i >= switchNum or switchList[s - i] != switchList[s + i]:
            return
        switchList[s - i] = (switchList[s - i] + 1) % 2
        switchList[s + i] = (switchList[s + i] + 1) % 2


for _ in range(stdNum):
    g, s = map(int, input().split())
    if g == 1:
        calcOne(s)
    if g == 2:
        calcTwo(s - 1)

for i in range(switchNum):
    print(switchList[i], end=" " if i % 20 != 19 else "\n")

