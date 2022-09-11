def solution(n):
    a = 1
    b = 1    
    for i in range(2, n + 1):
        c = b
        b = a + b
        a = c
    
    return b % 1234567