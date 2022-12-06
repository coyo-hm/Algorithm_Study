import sys
input = sys.stdin.readline
n = int(input())
array = [(2, 2), (1, 1), (1, 2)]
d = [0] * (n + 1)
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
  d[i] = (d[i - 1] + d[i - 2] * 2) % 796796
    
print(d[n])