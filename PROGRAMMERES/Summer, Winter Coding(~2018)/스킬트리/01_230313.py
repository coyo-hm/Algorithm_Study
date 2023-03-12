def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skills = "".join([s for s in skills if s in skill])
        if (skills in skill and skill[0] in skills) or len(skills) == 0:
            answer += 1
    return answer