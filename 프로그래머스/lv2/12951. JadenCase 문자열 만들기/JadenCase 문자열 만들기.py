def solution(s):
    ans = ''
    for i in range(len(s)):
        if i == 0 and i != ' ':
            ans += s[i].upper()
        else:
            if s[i-1] == ' ' and s[i] != ' ':
                ans += s[i].upper()
            else:
                ans += s[i].lower()
    return ans