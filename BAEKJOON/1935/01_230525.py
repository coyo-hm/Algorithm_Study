import sys
input = sys.stdin.readline
n = int(input())
exp = list(input().rstrip())
nums = [int(input()) for _ in range(n)]

number = []

for e in exp:
    # print(number)
    if "A" <= e <= "Z":
        number.append(nums[ord(e) - ord("A")])
    else:
        a = number.pop()
        b = number.pop()
        if e == "+":
            number.append(a + b)
        elif e == "-":
            number.append(b - a)
        elif e == "*":
            number.append(a * b)
        elif e == "/":
            number.append(round(b / a, 2))

print(format(number[0], ".2f"))