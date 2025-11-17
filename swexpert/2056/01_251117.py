# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5QLkdKAz4DFAUq&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20
# 00:12:34

T = int(input())

def is_date(month, date):
    if month == 0 or date == 0:
        return False
    if month == 2 and date > 28:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and date > 31:
        return False
    if month in [4, 6, 9, 11] and date > 30:
        return False
    return True


for test_case in range(1, T + 1):
    _input = input().rstrip()
    year, month, date = map(int, [_input[0:4], _input[4:6], _input[6:]])
    if is_date(month, date):
        print("#{0}".format(test_case), "{0:04d}/{1:02d}/{2:02d}".format(year, month, date))
    else:
        print("#{0}".format(test_case), -1)
