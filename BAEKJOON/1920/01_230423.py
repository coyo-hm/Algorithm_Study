import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
mx = list(map(int, input().split()))

a.sort()

def findX(x):
    s = 0
    e = n - 1

    while s <= e:
        mid = (s + e) // 2
        if a[mid] == x:
            return 1
        if a[mid] > x:
            e = mid - 1
        elif a[mid] < x:
            s = mid + 1
    return 0


for x in mx:
    print(findX(x))