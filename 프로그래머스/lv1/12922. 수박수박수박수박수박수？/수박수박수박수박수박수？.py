def solution(n):
    p = ['수','박']
    l = p*int(n/2) if n%2 == 0 else p*int((n-1)/2)+['수']
    return ''.join(l)