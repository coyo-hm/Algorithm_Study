import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    num_list = "".join(["" + convert(i, n) for i in range(m * t)])    
    answer = ''.join([num_list[i * m + p - 1].upper() for i in range(t)])
        
    
    
    return answer