# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Pl0Q6ANQDFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:04:31


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = [0, 0, 0, 0, 0]
    pri = [2, 3, 5, 7, 11]
    i = 0
    while n > 1 and i < 5:
        if n % pri[i] == 0:
            n = n // pri[i]
            answer[i] += 1
        else:
            i += 1

    print("#{0}".format(test_case), " ".join(map(str, answer)))
