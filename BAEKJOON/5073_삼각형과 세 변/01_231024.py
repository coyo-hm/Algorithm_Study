import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a + b + c == 0:
        break

    m = max([a, b, c])
    s = sum([a, b, c])

    if m >= s - m:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")