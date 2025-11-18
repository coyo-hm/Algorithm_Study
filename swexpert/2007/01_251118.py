# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5P1kNKAl8DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:17:30

MAX_LENGTH = 10

T = int(input())
for test_case in range(1, T + 1):
    _input = input().rstrip()
    for i in range(1, MAX_LENGTH + 1):
        word = _input[0:i]
        if _input in word * 30:
            print("#{0}".format(test_case), i)
            break
