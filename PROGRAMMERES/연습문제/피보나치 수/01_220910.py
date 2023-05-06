def solution(n):
    Fibo = [0, 1, 1]
    for i in range(3, n + 1):
        Fibo.append(Fibo[i - 1] + Fibo[i - 2])   
    div = 1234567
    return Fibo[n] % div