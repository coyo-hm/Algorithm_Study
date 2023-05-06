def solution(price, money, count):
    pay = sum([price * (i + 1) for i in range(count)])
    return pay - money if pay > money else 0