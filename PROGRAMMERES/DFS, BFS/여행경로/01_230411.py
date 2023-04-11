def solution(tickets):
    airport = {}
    stack = ["ICN"]
    ans = []

    for t in tickets:
        airport[t[0]] = airport.get(t[0], []) + [t[1]]

    for a in airport:
        airport[a].sort(reverse = True)

    while stack:
        top = stack[-1]
        if top not in airport or len(airport[top]) == 0:
            ans.append(stack.pop())
        else:
            stack.append(airport[top][-1])
            airport[top] = airport[top][:-1]

    return ans[::-1]