from heapq import heappush, heapify, heappop

def calcTime(time):
    [h, m] = time.split(":")
    h = int(h)
    m = int(m)
    return h * 60 + m

def solution(book_time):
    book_time.sort()
    answer = 0
    room = []
    heapify(room)

    for s, e in book_time:
        if room and room[0] <= calcTime(s):
            heappop(room)
            heappush(room, calcTime(e) + 10)
        else:
            heappush(room, calcTime(e) + 10)
        answer = max(answer, len(room))

    return answer