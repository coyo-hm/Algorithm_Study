def GCD(a, b):
    if b == 0: 
        return a
    else:
        return GCD(b, a % b)
def LCM(a, b):
    gcd = GCD(a, b)    
    return a * b // gcd

def solution(arr):
    a = arr.pop()
    b = arr.pop()
    lcm = LCM(a, b)
    for i in arr:
        lcm = LCM(lcm, i)
    return lcm