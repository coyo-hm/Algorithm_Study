# https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 33:12

from collections import defaultdict


def solution(edges):
    out_deg = defaultdict(list)
    in_deg = defaultdict(list)
    nodes = set()

    # 진출차수 / 진입차수 계산
    for a, b in edges:
        out_deg[a].append(b)
        in_deg[b].append(a)
        nodes.add(a)
        nodes.add(b)

    # 생성된 정점 찾기 : out >= 2, in == 0
    created_node = None
    for v in nodes:
        if len(in_deg[v]) == 0 and len(out_deg[v]) >= 2:
            created_node = v
            break

    donut = bar = eight = 0

    # 생성된 정점에서 나가는 간선 개수 = 전체 그래프 수
    total = len(out_deg[created_node])

    # 각 노드의 차수를 통해 그래프 종류 판별
    for v in nodes:
        o = len(out_deg[v]) if created_node not in out_deg[v] else len(out_deg[v]) - 1
        i = len(in_deg[v]) if created_node not in in_deg[v] else len(in_deg[v]) - 1
        # o, i = out_deg[v], in_deg[v]
        if v == created_node:
            continue

        # 막대 그래프: out=0, in=1인 정점 존재
        if o == 0 and i <= 1:
            bar += 1
        # 8자 그래프: out=2, in>=2인 정점 존재
        elif o == 2 and i >= 2:
            eight += 1

    # 도넛 그래프 수 = 전체 그래프 수 - 막대 - 8자
    donut = total - bar - eight

    return [created_node, donut, bar, eight]
