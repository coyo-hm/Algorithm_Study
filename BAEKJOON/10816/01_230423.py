import sys

input = sys.stdin.readline
n = int(input())
nc = list(map(int, input().split()))
m = int(input())
mCard = list(map(int, input().split()))

nc.sort()

cnt = 1
inc = nc[0]

cardList = []

for i in range(1, n):
    if nc[i] != inc:
        cardList.append((inc, cnt))
        cnt = 1
        inc = nc[i]
    else:
        cnt += 1

if cnt != 0:
    cardList.append((inc, cnt))

# print(cardList)

def findx(x):
    s = 0
    e = len(cardList) - 1
    while s <= e:
        mid = (s + e) // 2
        if cardList[mid][0] == x:
            print(cardList[mid][1], end=" ")
            return
        if cardList[mid][0] > x:
            e = mid - 1
        elif cardList[mid][0] < x:
            s = mid + 1
    print(0, end=" ")


for mc in mCard:
    findx(mc)
