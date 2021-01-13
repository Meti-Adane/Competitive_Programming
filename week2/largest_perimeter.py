def largestPerimeter(A) -> int:
    i = 0
    possibleCombinations = []
    while i < 3 and A != []:
        max_num = max(A)
        possibleCombinations.append(max_num)
        A.remove(max_num)
        i += 1
        if i > 2:
            s = sum(possibleCombinations) / 2
            for k in possibleCombinations:
                if k >= s or s-k == 0:
                    possibleCombinations.remove(k)
                    i -= 1
    if len(possibleCombinations) == 3: return sum(possibleCombinations)
    else:  return 0