# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14_DEKAJcCFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:12:28


def pop_num(num_str):
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return num_str[:i] + num_str[i + 2:]
    return num_str


T = 10
for test_case in range(1, T + 1):
    n, str = input().split()
    prev, curr = "", str

    while prev != curr:
        prev = curr
        curr = pop_num(curr)

    print("#{0}".format(test_case), curr)
