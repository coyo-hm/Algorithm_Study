def solution(today, terms, privacies):
    [y, m, d] = today.split(".")
    numToday = int(d) + int(m) * 28 + int(y) * 12 * 28
    expiryDate = {}
    answer = []
    for term in terms:
        [t, m] = term.split()
        expiryDate[t] = int(m) * 28
    for i in range(len(privacies)):
        [dateStr, term] = privacies[i].split()
        date = dateStr.split(".")
        d = int(date[0]) * 28 * 12 + int(date[1]) * 28 + int(date[2])
        if d + expiryDate[term] <= numToday:
            answer.append(i + 1)
    
    return answer