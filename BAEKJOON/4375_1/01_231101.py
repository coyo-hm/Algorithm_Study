import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        num = int("1" * len(str(n)))

        while num % n != 0:
            num = num * 10 + 1
        print(len(str(num)))
    except:
        break