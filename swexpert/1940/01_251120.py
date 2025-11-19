# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PjMgaALgDFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:11:30

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = 0
    curr_speed = 0
    for _ in range(n):
        _input = list(map(int, input().split()))
        command = _input[0]
        speed = 0 if len(_input) == 1 else _input[1]
        if command == 1:
            curr_speed += speed

        elif command == 2:
            curr_speed = max(curr_speed - speed, 0)
        answer += curr_speed
    print("#{0}".format(test_case), answer)
