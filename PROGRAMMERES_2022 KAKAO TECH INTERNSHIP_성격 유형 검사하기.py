def solution(survey, choices):
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M":0, "A": 0,"N":0}
    
    for i in range(len(choices)):
        if(choices[i] < 4):
            score[survey[i][1]] += choices[i] - 4
        elif(choices[i] > 4):
            score[survey[i][0]] += 4 - choices[i]
        
    answer = ("T" if score["R"] < score["T"] else "R") + ("F" if score["C"] < score["F"] else "C") + ("M" if score["J"] < score["M"] else "J") +  ("N" if score["A"] < score["N"] else "A")
    
    return answer