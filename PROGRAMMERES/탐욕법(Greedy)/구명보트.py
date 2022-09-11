
def solution(people, limit):
    people.sort(reverse = True)
    answer = len([i for i in people if people[-1] + i > limit])
    people = people[answer:]
    for p in people:
        # print(people, p)
        if p + people[-1] <= limit:
            people.pop()
        answer += 1
        
        
    return answer