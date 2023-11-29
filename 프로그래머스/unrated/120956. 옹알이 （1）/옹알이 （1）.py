def solution(babbling):
    answer = 0
    talk = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        for t in talk:
            if t in babble:
                babble = babble.replace(t, '1')
        if babble.isdigit() is True:
            answer += 1
    return answer