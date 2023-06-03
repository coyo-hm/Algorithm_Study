# https://school.programmers.co.kr/learn/courses/30/lessons/77885#
def func(number):
    b = "00" + bin(number)[2:]
    l = len(b)
    for i in range(l - 1, -1, -1):
        if b[i] == "0":
            c = 2 ** (l - 1 - i)
            return number + c - c // 2


def solution(numbers):
    answer = []
    for n in numbers:
        ans = n + 1 if n % 2 == 0 else func(n)
        answer.append(ans)
    return answer