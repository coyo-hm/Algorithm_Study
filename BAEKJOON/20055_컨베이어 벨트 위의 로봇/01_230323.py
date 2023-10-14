import sys
import collections

input = sys.stdin.readline

n, k = map(int, input().split())
belt = collections.deque(list(map(int, input().split())))
robot = collections.deque([0] * n)


cnt = 0

while True:
  robot.rotate(1)
  belt.rotate(1)
  robot[-1] = 0
  if sum(robot):
    for i in range(n - 2, -1, -1):
      if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] > 0:
        robot[i + 1] = 1
        robot[i] = 0
        belt[i + 1] -= 1
    robot[-1] = 0
  if robot[0] == 0 and belt[0] > 0:
    robot[0] = 1
    belt[0] -= 1
  cnt += 1
  if belt.count(0) >= k:
    break

print(cnt)
