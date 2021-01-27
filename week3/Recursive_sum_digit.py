# question url: https://www.hackerrank.com/challenges/recursive-digit-sum/problem
def super(n, k):
    s = 0
    if k == 1:
        return n
    for i in n:
        s += int(i)
    s = str(s)
    return super(s, len(s))

def superDigit(n, k):
    s = 0
    for i in n:
        s = s + int(i)
    s = s * k
    s = str(s)
    r = super(s, k)
    return r