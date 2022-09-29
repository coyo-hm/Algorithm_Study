y, x = input()

x = int(x) - 1
y = ord(y) - ord("a")

steps=[(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

cnt = 0

for dx, dy in steps:
  if 0 <= dx + x < 8 and 0 <= dy + y < 8:
    cnt += 1

print(cnt)