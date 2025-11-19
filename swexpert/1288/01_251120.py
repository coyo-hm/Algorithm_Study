# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV18_yw6I9MCFAZN&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:16:16

def decompose_num(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n = n // 10
    return arr


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = n
    num_set = set([])

    while len(num_set) < 10:
        arr = decompose_num(answer)
        num_set.update(arr)
        answer += n

    print("#{0}".format(test_case), answer - n)
