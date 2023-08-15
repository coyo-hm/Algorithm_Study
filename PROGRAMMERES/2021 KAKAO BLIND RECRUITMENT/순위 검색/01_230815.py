def solution(infos, queries):
    answer = []
    info_dict = {}
    for lang in ["cpp", "java", "python", "-"]:
        for job in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    info_dict[lang + job + career + food] = []
    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        info_dict[lang + job + career + food].append(int(info[4]))
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.replace(" and", "").split(" ")
        score = int(query[4])
        query = "".join(query[:4])
        res = info_dict[query]
        l, r = 0, len(res) - 1
        while l <= r:
            m = (l + r) // 2
            if res[m] < score:
                l = m + 1
            else:
                r = m - 1
        answer.append(len(res) - l)

    return answer