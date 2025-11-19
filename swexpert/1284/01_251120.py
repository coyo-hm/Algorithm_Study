# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV189xUaI8UCFAZN&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 03:40


T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    price_A = P * W
    price_B = Q + (W - R) * S if W > R else Q
    print("#{0}".format(test_case), min(price_A, price_B))
