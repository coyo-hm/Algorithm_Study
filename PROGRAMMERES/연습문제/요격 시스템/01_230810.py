def solution(targets):
    targets.sort()
    m = [0]

    for s, e in sorted(targets):
        if m[-1] <= s:
            m.append(e)
        else:
            m[-1] = min(m[-1], e)

    return len(m) - 1
