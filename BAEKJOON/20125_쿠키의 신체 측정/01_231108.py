import sys
input = sys.stdin.readline
N = int(input())
head = (-1, -1)
heart = (-1, -1)
waist = 0
left_arm, right_arm = 0, 0
left_leg, right_leg = 0, 0

for r in range(N):
    col = list(input().rstrip())
    for c in range(N):
        if col[c] == "*":
            if head == (-1, -1):
                head = (r, c)
                heart = (r + 1, c)
            elif heart[1] > c and heart[0] == r:
                left_arm += 1
            elif heart[1] < c and heart[0] == r:
                right_arm += 1
            elif heart[1] == c and heart[0] < r:
                waist += 1
            elif heart[1] > c and heart[0] < r:
                left_leg += 1
            elif heart[1] < c and heart[0] < r:
                right_leg += 1

print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)