from collections import deque
def solution(cacheSize, cities):
    cache = deque(maxlen = cacheSize)
    t = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            t += 1
            cache.remove(s)
            cache.append(s)

        else:
            t += 5
            cache.append(s)
    return t