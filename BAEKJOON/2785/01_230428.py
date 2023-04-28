import sys
import collections
input = sys.stdin.readline
n = int(input())
ls = collections.deque(list(map(int, input().split())))
ls.sort()
cnt = 0





print(cnt)