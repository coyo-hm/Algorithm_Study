import math

def calcTime(time):
    [h, m] = time.split(":");
    return int(h) * 60 + int(m)

def calcFees(fees, t):
    p = math.ceil((t - fees[0]) / fees[2])
    return p * fees[3] + fees[1] if p > 0 else fees[1]

def solution(fees, records):
    answer = []
    cars = {}
    s_cars = {}
    f_cars = {}
    for r in records:
        [strTime, car, bd] = r.split()
        if bd == "IN":
            s_cars[car] = calcTime(strTime)
            f_cars[car] = True
            if car not in cars:
                cars[car] = 0
        else:
            cars[car] += (calcTime(strTime) - s_cars[car])
            f_cars[car] = False
    
    for car in sorted(cars):
        c = cars[car]
        if f_cars[car]:
            c += (calcTime("23:59") - s_cars[car])
        answer.append(calcFees(fees, c))
        
    return answer