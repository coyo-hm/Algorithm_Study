# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14jJh6ACYCFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:07:43

NUM_CHART = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}

T = int(input())
for _ in range(1, T + 1):
    test_case, length = input().split()
    arr = input().split()
    test_case = int(test_case[1:])
    arr.sort(key=lambda x: NUM_CHART[x])
    print("#{0}".format(test_case), " ".join(arr))
