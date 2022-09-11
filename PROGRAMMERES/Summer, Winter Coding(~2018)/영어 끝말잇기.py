def solution(n, words):
    people = 0
    num = 0
    l = ""
    
    for i, w in enumerate(words):
        if i != 0 and (w[0] != l or words[:i].count(w) != 0):
            # print(w[0], l, w)
            people = i % n + 1
            num = i // n + 1
            break
        l = w[-1]
    return [people, num]