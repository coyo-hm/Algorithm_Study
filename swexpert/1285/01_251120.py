# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV18-stqI8oCFAZN&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(abs, map(int, input().split())))
    min_distance = min(arr)
    cnt = arr.count(min_distance)
    print("#{0}".format(test_case), min_distance, cnt)
