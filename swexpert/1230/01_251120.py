# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14zIwqAHwCFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14

# 00:27:56

from collections import deque

T = 10
for test_case in range(1, T + 1):
    origin_N = int(input())
    code = input().split()
    command_N = int(input())
    commands = deque(input().split())
    while commands:
        command = commands.popleft()
        if command == "I":
            x = int(commands.popleft())
            y = int(commands.popleft())
            curr = code[:x]
            for _ in range(y):
                curr.append(commands.popleft())
            curr += code[x:]
            code = curr.copy()
        elif command == "D":
            x = int(commands.popleft())
            y = int(commands.popleft())
            code = code[:x] + code[x + y:]
        else:
            y = int(commands.popleft())
            for _ in range(y):
                code.append(commands.popleft())

    print("#{0}".format(test_case), " ".join(code[:10]))
