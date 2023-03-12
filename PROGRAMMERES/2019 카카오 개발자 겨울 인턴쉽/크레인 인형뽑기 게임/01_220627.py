def solution(board, moves):
    answer = 0
    basket = []

    for i in moves:
        idx = i - 1
        for j in range(len(board)):
            if(board[j][idx] != 0):
                temp = board[j][idx]
                board[j][idx] = 0
                if(len(basket) != 0 and basket[len(basket) - 1] == temp):
                    answer += 2
                    basket.pop()
                else:
                    basket.append(temp)
                break;


    return answer