def solution(s):
    return len(s) == len([i for i in s if i >= "0" and i <= "9"]) and (len(s) == 4 or len(s) == 6)