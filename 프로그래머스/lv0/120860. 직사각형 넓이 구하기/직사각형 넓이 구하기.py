def solution(dots):
    xs, ys = [], []
    for dot in dots:
        x, y = dot
        if x not in xs:
            xs.append(x)
        if y not in ys:
            ys.append(y)
    return abs(xs[0]-xs[1])*abs(ys[0]-ys[1])