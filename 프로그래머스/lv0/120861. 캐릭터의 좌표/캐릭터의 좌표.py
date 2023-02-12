def solution(keyinput, board):
    answer = []
    x = 0
    y = 0
    row = (board[0]-1)/2
    col = (board[1]-1)/2
    
    for i in keyinput:
        if i == 'left' and -row<= (x-1) <= row :
            x -= 1
        elif i == 'right' and -row<= (x+1) <= row :
            x += 1
        elif i == 'up' and -col<= (y+1) <= col:
            y += 1
        elif i == 'down' and -col<= (y-1) <= col:
            y -= 1
    return [x,y]