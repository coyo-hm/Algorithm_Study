def solution(want, number, discount):
    answer = 0
    wish = {}
    for i in range(len(want)):
        wish[want[i]] = number[i]
    for i in range(len(discount) - 9):
        temp = 0
        for j in want:
            if discount[i:i+10].count(j) >= wish[j]:
                temp += 1
        if temp == len(wish):
            answer += 1
    return answer