def solution(a, b):
    weeks = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b + 4
    if a - 1 > 0:
        day += sum(days[: a - 1])    
    return weeks[day % 7]