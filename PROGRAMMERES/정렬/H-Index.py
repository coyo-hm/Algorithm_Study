def solution(citations):
    citations.sort(reverse = True)
    for c in range(citations[0], -1, -1):
        if len([i for i in citations if i >= c]) >= c:
            return c