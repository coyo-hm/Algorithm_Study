def solution(s, n):
    answer = []
    for i in s:
        if "a" <= i and "z" >= i:
            answer.append(chr((ord(i) + n - ord("a"))% 26 + ord("a") ))
            
        elif "A" <= i and "Z" >= i:
            answer.append(chr((ord(i) + n - ord("A"))% 26 + ord("A") ))
        else:
            answer.append(" ")
    return "".join(answer)