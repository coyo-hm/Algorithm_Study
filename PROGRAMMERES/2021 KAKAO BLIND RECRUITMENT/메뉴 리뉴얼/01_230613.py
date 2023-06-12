import itertools


def solution(orders, course):
    answer = []
    for c in course:
        dic = {}
        for order in orders:
            if len(order) < c:
                continue
            for m in list(itertools.combinations(order, c)):
                m = "".join(sorted(m))
                if m in dic:
                    dic[m] += 1
                else:
                    dic[m] = 1
        sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        m = sorted_dic[0][1] if (len(sorted_dic) > 0) else 0
        for s in sorted_dic:
            if s[1] >= m and s[1] >= 2:
                answer.append(s[0])

    answer.sort()
    return answer