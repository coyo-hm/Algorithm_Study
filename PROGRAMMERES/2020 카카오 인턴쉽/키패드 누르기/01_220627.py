def solution(numbers, hand):
    answer = ''
    l_list = [1, 4, 7]
    r_list = [3, 6, 9]
    h_loc = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    l = (3, 0)
    r = (3, 2)

    for i in numbers:
        if i in l_list:
            answer += 'L'
            l = h_loc[i]
        elif i in r_list:
            answer += 'R'
            r = h_loc[i]
        else:
            # print(i, h_loc[i], l, abs(h_loc[i][0] - l[0]) + abs(h_loc[i][1] - l[1]), r, abs(h_loc[i][0] - r[0]) + abs(h_loc[i][1] - r[1]))
            if abs(h_loc[i][0] - l[0]) + abs(h_loc[i][1] - l[1]) < abs(h_loc[i][0] - r[0]) + abs(h_loc[i][1] - r[1]):
                answer += 'L'
                l = h_loc[i]
            elif abs(h_loc[i][0] - l[0]) + abs(h_loc[i][1] - l[1]) > abs(h_loc[i][0] - r[0]) + abs(h_loc[i][1] - r[1]):
                answer += 'R'
                r = h_loc[i]
            else:
                if hand == "right":
                    answer += 'R'
                    r = h_loc[i]
                else:
                    answer += 'L'
                    l = h_loc[i]
    return answer