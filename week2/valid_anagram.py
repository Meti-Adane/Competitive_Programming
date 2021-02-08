def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    for i in s:
        if i not in t or s.count(i) != t.count(i): return False
        print(t.count(i), s.count(i))
    for j in t:
        if j not in s or t.count(j) != s.count(j): return False
    return True