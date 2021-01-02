def counter(steps,path):
    is_valid=True
    for i in path:
        if i not in 'UD':
            is_valid=False
            break
    if steps < 2 or steps>10**6 or len(path) != steps or is_valid==False:
        return 0

    else:
        slope = 0
        valley = 0
        for i in path:
            if i == 'U':
                slope += 1
            elif i == 'D':
                slope -= 1
            if i == 'U' and slope == 0:
                valley += 1
        return(valley)



