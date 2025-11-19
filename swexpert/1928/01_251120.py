# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PR4DKAG0DFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:33:50

def step_one(l):
    if l == "+":
        return 62
    if l == "/":
        return 63
    o = ord(l)
    if ord("0") <= o <= ord("9"):
        return o - ord("0") + 52
    if ord("A") <= o <= ord("Z"):
        return o - ord("A")
    if ord("a") <= o <= ord("z"):
        return o - ord("a") + 26


T = int(input())
for test_case in range(1, T + 1):
    encoding_str = input().rstrip()
    decoding_str = ""
    answer = ""
    num_A, num_a = ord("A"), ord("a")
    for s in encoding_str:
        n = step_one(s)
        decoding_str += str(bin(n))[2:].zfill(6)
    for s in range(0, len(decoding_str), 8):
        n = int(decoding_str[s:s + 8], 2)
        answer += chr(n)

    print("#{0}".format(test_case), answer)
