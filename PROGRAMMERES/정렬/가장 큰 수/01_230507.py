from functools import cmp_to_key


def compare(a, b):
    sa = str(a)
    sb = str(b)
    return int(sb + sa) - int(sa + sb)


def solution(numbers):
    answer = ""
    arr = sorted(numbers, key = cmp_to_key(compare))

    if arr[0] == 0:
        return "0"

    for n in arr:
        answer += str(n)
    return answer