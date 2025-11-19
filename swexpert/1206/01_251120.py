# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV134DPqAA8CFAYh&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:10:39

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    for i in range(2, N - 2):
        left = buildings[i] - max(buildings[i - 2:i])
        right = buildings[i] - max(buildings[i + 1: i + 3])
        if left < 0 or right < 0:
            continue
        answer += min(left, right)
    print("#{0}".format(test_case), answer)
